# G3 Trial 09｜Behavior Change Evidence Ledger v1

```yaml
trial_id: YL-TRILOGY-GENERAL-v2-TRIAL-09-G3-LIVE
status: WAITING_FOR_REAL_EVIDENCE
claim_policy: behavior_change_requires_observable_evidence
```

> “觉得有启发”“很认同”“准备以后用”均不算 Behavior Change。只记录已经发生、可描述、可回看或可被他人复判的真实变化。

## Evidence classes

可接受的最小证据包括：

- `DEC_CHANGE`：真实决策改变；
- `REJECT_CHANGE`：真实拒绝/停止一个原计划；
- `SAVE_CHANGE`：把一次经验转化为可再次调用的结构；
- `ACT_CHANGE`：下一真实行动改变；
- `PRELOAD_CHANGE`：下一任务前主动加载上一轮 Learning；
- `NO_CHANGE`：诚实记录没有变化。

## P__

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

若声称上一轮 Learning 被复用，必须额外记录：

```yaml
learning_ref: NOT_OBSERVED
preloaded_before_next_decision: NOT_OBSERVED
next_task_is_distinct_real_task: NOT_OBSERVED
actual_use: NOT_OBSERVED
changed_decision: NOT_OBSERVED
changed_wpk: NOT_OBSERVED
changed_action: NOT_OBSERVED
```

只有满足“真实 Task2 + 事前 preload + actual use + 至少一项 DEC/WPK/ACT 改变”时，才可标记：

```yaml
reuse_candidate: true
```

这仍不自动授权 `compounding_proven`，须进入 Evidence Settlement 和 Fresh Human Gate。

## Aggregate

```yaml
participants_with_observable_behavior_change: NOT_OBSERVED
total_participants: NOT_OBSERVED
majority_behavior_change_signal: NOT_OBSERVED
reuse_candidates: NOT_OBSERVED
compounding_proven: false
```