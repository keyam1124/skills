# 実行方式のDesign Memo

## Evidence

- 利用者はAntigravity CLIによる実行を指定している。
- `agy models` で `gemini-3.8-flash-medium` を確認できた。

## Inference

CLIが存在しても認証やモデルの利用に失敗する場合がある。

## Decision

`agy` で指定モデルを実行し、失敗したら停止する。文書は標準入力で渡し、作業ディレクトリは一時ディレクトリにする。標準出力の結果を検証し、空の応答やツールが使われた応答は採用しない。

## Human confirmation

CLIの認証や利用制限の問題は利用者に報告する。
