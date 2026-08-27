# G3 Trial 09｜Behavior Change Evidence Ledger v1.1

```yaml
trial_id: YL-TRILOGY-GENERAL-v2-TRIAL-09-G3-LIVE
status: L2_FORMAL_VALIDATION_TOOL_NOT_REQUIRED_FOR_CURRENT_CLAIM
claim_policy: behavior_change_requires_observable_evidence
mandatory_for_every_session: false
```

> “觉得有启发”“很认同”“准备以后用”仍然不算 Behavior Change。
>
> 但本 Ledger 不再作为每次真人课后的必填行政动作。系统优先从后续自然发生的决策、作业、聊天、行动和主动复用中捕捉行为变化候选。

## L0 / L1 如何处理 Behavior

### L0 自然证据

如果学员在后续真实互动中自然说出或表现出：

- 改了一个决策；
- 停掉一个原计划；
- 保存了一个方法；
- 改了下一步行动；
- 主动把上一轮 Learning 带进新任务；

系统可记录为 `behavior_change_candidate`，无需讲师额外让学员填表。

### L1 轻验证

如果这条行为候选会改变当前课程判断，只需自然追问：

> **“你原来准备怎么做？现在具体改了什么？”**

AI / OS 负责结构化为候选 Evidence。

## L2 正式验证

只有要做正式效果声明、Promotion、Reuse / Compounding 证明时，才启用完整字段。

可接受 Evidence Classes：

- `DEC_CHANGE`：真实决策改变；
- `REJECT_CHANGE`：真实拒绝 / 停止一个原计划；
- `SAVE_CHANGE`：把一次经验转化为可再次调用的结构；
- `ACT_CHANGE`：下一真实行动改变；
- `PRELOAD_CHANGE`：下一任务前主动加载上一轮 Learning；
- `NO_CHANGE`：诚实记录没有变化。

## P__ Formal Record

```yaml
pid: P__
evidence_class: NOT_OBSERVED
observed_at: NOT_OBSERVED
related_value_thread_id: NOT_OBSERVED
previous_intent_or_default: NOT_OBSERVED
actual_changed_decision_or_action: NOT_OBSERVED
evidence_ref: NOT_OBSERVED
self_report_only: NOT_OBSERVED
independent_recheck_possible: NOT_OBSERVED
```

描述：______

### Reuse boundary

若声称上一轮 Learning 被复用，必须额外满足：

```yaml
learning_ref: NOT_OBSERVED
preloaded_before_next_decision: NOT_OBSERVED
next_task_is_distinct_real_task: NOT_OBSERVED
actual_use: NOT_OBSERVED
changed_decision: NOT_OBSERVED
changed_wpk: NOT_OBSERVED
changed_action: NOT_OBSERVED
```

只有满足“真实 Task2 + 事前 preload + actual use + 至少一项 DEC / WPK / ACT 改变”时，才可标记 `reuse_candidate: true`。

这仍不自动授权 `compounding_proven`，须进入 Evidence Settlement 和 Fresh Human Gate。

## Aggregate

```yaml
participants_with_observable_behavior_change: NOT_OBSERVED
total_participants: 5
majority_behavior_change_signal: NOT_OBSERVED
reuse_candidates: NOT_OBSERVED
compounding_proven: false
```

当前 `NOT_OBSERVED` 不是失败，而是当前 L0 声明并不要求主动制造 L2 行为验证任务。
