#!/usr/bin/env python3
"""Heuristic Swift design hotspot scanner.

This is not a linter. It finds places worth reading before implementation,
refactoring, or review.
"""

from __future__ import annotations

import argparse
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SKIP_DIRS = {
    ".build",
    ".git",
    "Build",
    "DerivedData",
    "Pods",
    "Carthage",
    "SourcePackages",
    "xcuserdata",
}


@dataclass
class Finding:
    severity: str
    path: Path
    line: int
    message: str


def iter_swift_files(root: Path) -> Iterable[Path]:
    if root.is_file() and root.suffix == ".swift":
        yield root
        return

    for current, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.endswith(".xcodeproj")]
        for name in files:
            if name.endswith(".swift"):
                yield Path(current) / name


def scrub_code_line(line: str) -> str:
    """Remove comments and replace string literal contents on one line."""
    output: list[str] = []
    in_string = False
    escaped = False
    index = 0
    while index < len(line):
        char = line[index]
        next_char = line[index + 1] if index + 1 < len(line) else ""

        if not in_string and char == "/" and next_char == "/":
            break

        if char == '"' and not escaped:
            in_string = not in_string
            output.append('"')
        elif in_string:
            output.append(" ")
        else:
            output.append(char)

        escaped = in_string and char == "\\" and not escaped
        if char != "\\":
            escaped = False
        index += 1

    return "".join(output)


def find_matching_block(lines: list[str], start_index: int) -> int | None:
    depth = 0
    seen_open = False
    for index in range(start_index, len(lines)):
        line = scrub_code_line(lines[index])
        depth += line.count("{")
        if "{" in line:
            seen_open = True
        depth -= line.count("}")
        if seen_open and depth <= 0:
            return index
    return None


def scan_file(path: Path) -> list[Finding]:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    findings: list[Finding] = []

    if len(lines) > 350:
        findings.append(
            Finding(
                "warn",
                path,
                1,
                f"large Swift file ({len(lines)} lines); check whether multiple responsibilities are mixed",
            )
        )

    state_wrappers = 0
    type_decl_count = 0

    for index, raw_line in enumerate(lines, start=1):
        line = scrub_code_line(raw_line)
        stripped = line.strip()
        if not stripped:
            continue

        if re.match(r"(public |private |fileprivate |internal |final )*(struct|class|enum|actor)\s+\w+", stripped):
            type_decl_count += 1

        if re.search(r"\btry\s*!", line):
            findings.append(Finding("error", path, index, "uses try!; verify this cannot fail or replace with explicit error handling"))

        if re.search(r"\bas\s*!", line):
            findings.append(Finding("error", path, index, "uses forced cast; prefer typed model, guard cast, or explicit failure path"))

        if re.search(r"[\w\]\)\}]!\s*(?:[.\[,)]|$)", line) and not stripped.startswith("#"):
            findings.append(Finding("warn", path, index, "possible force unwrap; verify the invariant is explicit"))

        if re.search(r":\s*[A-Za-z_][A-Za-z0-9_<>\[\]:., ]*!\b", line):
            findings.append(Finding("warn", path, index, "implicitly unwrapped optional type; verify the lifecycle invariant is explicit"))

        if "static let shared" in line or "static var shared" in line:
            findings.append(Finding("warn", path, index, "singleton-style shared state; check testability and hidden dependency cost"))

        if "UserDefaults.standard" in line:
            findings.append(Finding("info", path, index, "direct UserDefaults access; consider injecting or isolating if logic is under test"))

        if "Date()" in line or "UUID()" in line:
            findings.append(Finding("info", path, index, "direct Date/UUID creation; inject clock/id generator when behavior needs deterministic tests"))

        if re.search(r"\b(AnyView|Any)\b", line):
            findings.append(Finding("info", path, index, "uses Any/AnyView; check whether type erasure is necessary"))

        if "DispatchQueue.main.async" in line:
            findings.append(Finding("warn", path, index, "manual main dispatch; prefer MainActor boundaries in Swift concurrency code"))

        if re.search(r"\bfunc\s+\w+\s*\([^)]*\bBool\b", line):
            findings.append(Finding("info", path, index, "function has Bool parameter; consider enum/config type if it changes behavior branches"))

        if re.search(r"@(State|Binding|StateObject|ObservedObject|EnvironmentObject|AppStorage)\b", line):
            state_wrappers += 1

        if "TODO" in line or "FIXME" in line:
            findings.append(Finding("info", path, index, "contains TODO/FIXME; decide whether it is relevant to the current change"))

        if re.search(r"\bprint\s*\(", line):
            findings.append(Finding("info", path, index, "print statement in Swift code; verify it is not leftover debug output"))

    if type_decl_count > 5:
        findings.append(
            Finding(
                "info",
                path,
                1,
                f"contains {type_decl_count} top-level type declarations; check whether the file still has a coherent theme",
            )
        )

    if state_wrappers > 8:
        findings.append(
            Finding(
                "warn",
                path,
                1,
                f"contains {state_wrappers} SwiftUI state wrappers; check ownership and data flow",
            )
        )

    for index, raw_line in enumerate(lines):
        stripped = scrub_code_line(raw_line).strip()
        if re.match(r"(public |private |fileprivate |internal |static |mutating |nonisolated )*func\s+\w+", stripped):
            end = find_matching_block(lines, index)
            if end is not None:
                length = end - index + 1
                if length > 80:
                    findings.append(
                        Finding(
                            "warn",
                            path,
                            index + 1,
                            f"long function ({length} lines); look for mixed validation, side effects, and formatting",
                        )
                    )

        if re.match(r"(public |private |fileprivate |internal |final )*(struct|class|enum|actor)\s+\w+", stripped):
            end = find_matching_block(lines, index)
            if end is not None:
                length = end - index + 1
                if length > 220:
                    findings.append(
                        Finding(
                            "warn",
                            path,
                            index + 1,
                            f"large type ({length} lines); verify the type owns one clear responsibility",
                        )
                    )

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan Swift files for design hotspots.")
    parser.add_argument("path", nargs="?", default=".", help="Swift file or directory to scan")
    parser.add_argument("--max-findings", type=int, default=80, help="maximum findings to print")
    args = parser.parse_args()

    root = Path(args.path).expanduser().resolve()
    swift_files = sorted(iter_swift_files(root))
    findings: list[Finding] = []
    for swift_file in swift_files:
        findings.extend(scan_file(swift_file))

    order = {"error": 0, "warn": 1, "info": 2}
    findings.sort(key=lambda item: (order.get(item.severity, 9), str(item.path), item.line))

    print(f"Scanned {len(swift_files)} Swift file(s). Found {len(findings)} hotspot(s).")
    for finding in findings[: args.max_findings]:
        try:
            display_path = finding.path.relative_to(Path.cwd())
        except ValueError:
            display_path = finding.path
        print(f"[{finding.severity}] {display_path}:{finding.line}: {finding.message}")

    if len(findings) > args.max_findings:
        print(f"... {len(findings) - args.max_findings} more finding(s) omitted; raise --max-findings to inspect.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
