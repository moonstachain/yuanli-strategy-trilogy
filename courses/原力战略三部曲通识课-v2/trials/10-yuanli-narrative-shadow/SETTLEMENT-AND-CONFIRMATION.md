# Trial 10｜Calibration Settlement + Confirmation Gate

```yaml
calibration_status: NOT_STARTED
confirmation_status: NOT_STARTED
lesson_standard_v2_authority: NONE
machine_contract_authority: NONE
rollout_authority: NONE
```

## 1. Calibration Settlement

必须在真实 3–8 人完成 T0 / 24h / 7d / 30d 可得证据后填写。

### 八态逐项裁决

| State | Evidence | Decision |
|---|---|---|
| 唤 | pending | KEEP / REVISE / MERGE / DROP / UNOBSERVABLE |
| 裂 | pending | KEEP / REVISE / MERGE / DROP / UNOBSERVABLE |
| 聚 | pending | KEEP / REVISE / MERGE / DROP / UNOBSERVABLE |
| 构 | pending | KEEP / REVISE / MERGE / DROP / UNOBSERVABLE |
| 辨 | pending | KEEP / REVISE / MERGE / DROP / UNOBSERVABLE |
| 生 | pending | KEEP / REVISE / MERGE / DROP / UNOBSERVABLE |
| 迁 | pending | KEEP / REVISE / MERGE / DROP / UNOBSERVABLE |
| 化 | pending | KEEP / REVISE / MERGE / DROP / UNOBSERVABLE |

### 七证逐项裁决

记录：

- 是否可稳定观察；
- 是否与现有 Trial 指标重复；
- 是否提供增量诊断；
- 是否导致不必要教学负担。

### Calibration 只允许三个总出口

```text
A. REVISE_AND_CONFIRM
   方法有明显增量价值，但必须按真人证据修订后再验证。

B. KEEP_AS_EXPLANATORY_ONLY
   方法适合作为教研解释框架，但不足以进入正式 Lesson Standard。

C. REJECT_BY_REALITY
   八态/七证没有足够可观察性或增量价值，停止 Promotion。
```

不得从第一轮直接跳到 `METHOD_REUSABLE`。

## 2. 第二轮 Confirmation

只有 Calibration = `REVISE_AND_CONFIRM` 才可开始。

第二轮至少改变一个维度：

- 不同学员；或
- 不同课程；或
- 不同核心概念。

禁止完全复用同一批学员、同一问题、同一答案环境来制造确认。

Confirmation 必须检验：

1. 修订后的状态是否更可观察；
2. 七证能否重复获得；
3. T+7d Transfer 是否跨不同内容成立；
4. T+30d Reality Use 是否至少出现真实使用/反证；
5. 原力叙事是否真正带来比 Lesson Standard v1 更好的诊断或课程改进决定。

## 3. Fresh Human Gate

Confirmation 后只允许：

```text
APPROVE_METHOD_REUSABLE
KEEP_AS_EXPLANATORY_ONLY
REVISE_AND_RETEST
REJECT_BY_REALITY
```

只有 `APPROVE_METHOD_REUSABLE` 才允许向 Soul 提出 Lesson Standard v2 Candidate。

## 4. PR-C 触发合同｜Soul Lesson Standard v2

PR-C 当前状态：`NOT_AUTHORIZED_NOT_CREATED`。

触发前提：

```text
Calibration complete
+ Confirmation complete
+ Fresh Human Gate = APPROVE_METHOD_REUSABLE
```

若触发，PR-C 只提出 Candidate：

```text
一课一次模型更新
↓
一课一念
↓
一念三幕
↓
一课一果
```

以及可选的 M0/M1、八态、T0/24h/7d/30d 字段。

PR-C 不自动修改 Constitution 或 A1-C4。

## 5. PR-D 触发合同｜Machine Contract

PR-D 当前状态：`NOT_AUTHORIZED_NOT_CREATED`。

只有 PR-C 经过独立 Human Gate 后才允许提出：

- `templates/curriculum/concept-lesson-card-template.md`
- `schemas/concept-lesson-card.schema.yaml`
- `skills/yuanli-content-engineering/SKILL.md`
- path-scoped CI / validator

顺序必须：

> **Method → Reality → Standard → Machine Contract**

禁止：

> **Method Idea → Schema 强制全仓迁移。**

## 6. 推广 Gate

大规模推广当前：`NOT_AUTHORIZED`。

未来推广顺序：

```text
原力三部曲
→ 三分钟原力通识
→ 原力人生
→ 原力财富
→ 其他课程
```

每条课程线都先做 Shadow / compatibility audit，再局部重编；不得一次性全仓大迁移。

## 7. 最终停止门

只要真实证据未完成：

```yaml
method_reusable: false
lesson_standard_v2: blocked
machine_contract: blocked
rollout: blocked
```

这不是项目未完成，而是方法论按 Reality First 正确停在证据门前。
