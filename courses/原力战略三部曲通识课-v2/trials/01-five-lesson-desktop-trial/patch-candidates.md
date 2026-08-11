# Patch Candidates｜课程修订候选队列

> 当前状态：EMPTY / READY_NOT_RUN

## 纪律

Round 1 完成前：

- 只登记，不修改冻结课程；
- 不因为单一 Persona 的偏好直接改课；
- P0/P1/P2 必须有 Session 证据；
- 优先最小修改，不用新增概念解决概念过载。

## Patch Schema

| Patch ID | Severity | Lesson | Misconception / Block | Evidence refs | Root cause | Minimal patch | Expected side effect | Regression target | Decision |
|---|---|---|---|---|---|---|---|---|---|

## Root Cause Vocabulary

优先使用：

- `definition_ambiguity`
- `sequence_error`
- `example_mismatch`
- `metaphor_overreach`
- `concept_overload`
- `tool_prompt_ambiguity`
- `handoff_failure`
- `canon_boundary_leak`
- `teacher_dependency`
- `redundancy`

## Severity

### P0｜必须修

- 正典/法权误读；
- 核心概念反向理解；
- 会诱发错误行动；
- 不修不能进入下一轮。

### P1｜应该修

- 明显认知过载；
- 工具无法独立完成；
- 叙事断裂；
- 90分钟结构明显失真。

### P2｜可优化

- 措辞；
- 案例；
- 视觉；
- 节奏微调。

## Patch Gate

每个 P0/P1 必须完整满足：

```text
Misconception / Block
→ Raw Evidence
→ Root Cause
→ Minimal Patch
→ Regression Test
```

没有 Regression Target 的 Patch 不得标记 DONE。
