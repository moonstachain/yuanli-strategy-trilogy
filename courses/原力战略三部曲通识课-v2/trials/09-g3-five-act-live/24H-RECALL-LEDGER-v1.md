# G3 Trial 09｜24h Recall Ledger v1

```yaml
trial_id: YL-TRILOGY-GENERAL-v2-TRIAL-09-G3-LIVE
status: WAITING_UNTIL_RECALL_TARGET
session_end_at_approx: 2026-08-18T12:00:00+08:00
recall_target_at_approx: 2026-08-19T12:00:00+08:00
participant_scope:
  - P01
  - P02
  - P03
  - P04
  - P05
pre_answering_forbidden: true
```

> 24h Recall 必须由真人在不看资料、不补标准答案的情况下完成。AI/讲师可记录，但不得提示。当前目标时间按讲师补记的约 12:00 课程结束时间冻结为次日约 12:00。

## P01–P05 Recall

每位学员单独执行同一套冻结问题；不得五人集体互相提示后再作答。

```yaml
session_end_at_approx: 2026-08-18T12:00:00+08:00
recall_target_at_approx: 2026-08-19T12:00:00+08:00
materials_visible: false
teacher_prompt_beyond_frozen_questions: false
```

对每位 P01–P05 分别记录：

```yaml
pid: P__
recall_started_at: NOT_OBSERVED
elapsed_hours: NOT_OBSERVED
```

### Q1｜五幕

问题：五节课如果只剩五个动作，是什么？

原话摘要：______

```yaml
five_act_recall: NOT_OBSERVED
```

目标概念：`重估 → 入世 → 留存 → 继承 → 定向`。

### Q2｜价值生命史

问题：一个独特价值怎样从“我看见”走到“值得长期复利”？

原话摘要：______

```yaml
world_selection_present: NOT_OBSERVED
assetization_present: NOT_OBSERVED
os_learning_present: NOT_OBSERVED
direction_present: NOT_OBSERVED
```

### Q3｜时间为何不自动复利

问题：为什么一家经营十年的公司，可能并没有拥有十年的复利？

原话摘要：______

```yaml
time_entropy_understood: NOT_OBSERVED
```

### Q4｜State Transition

问题：举一个你自己的例子——过去一次真实经历，下一次应该因此怎样不同？

```text
Reality / Outcome：______
Learning：______
Next Task：______
Decision / Action change：______
```

```yaml
state_transition_real_example: NOT_OBSERVED
```

### Q5｜过去24h真实变化

问题：过去24小时，哪一个真实判断、拒绝、保存或行动已经变化？

原话摘要：______

```yaml
behavior_change_claimed: NOT_OBSERVED
behavior_change_evidence_ref: NOT_OBSERVED
```

## Recall integrity

每位学员分别记录：

```yaml
answer_leakage: NOT_OBSERVED
teacher_rescue: NOT_OBSERVED
participant_independent: NOT_OBSERVED
```

## Participant recall verdict

只允许：

```text
PASS
PARTIAL
FAIL
INVALID
NOT_RUN
```

当前：

```yaml
P01: NOT_RUN
P02: NOT_RUN
P03: NOT_RUN
P04: NOT_RUN
P05: NOT_RUN
```

在 2026-08-19 约 12:00 前，不因即时认可度高而预填任何 Recall 结果。