# Regression Cases

## Avoid blanket wrapping

Request: `全てのStringをValue Objectにしてください`

Expected:

- 機械的な全ラップを拒み、不変条件、取り違えリスク、複合値、ドメイン操作で候補を絞る。
- 一時変数、表示文言、局所値はprimitive維持候補にする。

## Distinguish typed IDs from full Value Objects

Request: `UserIdとOrderIdはDDDのValue Objectとして振る舞いも持たせるべき？`

Expected:

- 取り違え防止が主目的ならtyped id/newtype/branded typeで足りる可能性を示す。
- 検証やドメイン操作が自然にある場合だけsmart constructorや振る舞い付きValue Objectへ上げる。

## Keep DTO boundaries stable

Request: `APIレスポンスにもMoneyクラスをそのまま出したい`

Expected:

- 外部I/FはDTO/primitive表現を保つ判断を優先する。
- アプリケーション層でValue ObjectとDTOの相互変換を置く。
