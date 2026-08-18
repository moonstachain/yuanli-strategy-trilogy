# G3 Trial 09｜真人试讲执行账本 v1

```yaml
trial_id: YL-TRILOGY-GENERAL-v2-TRIAL-09-G3-LIVE
issue: moonstachain/yuanli-strategy-trilogy#19
status: LIVE_COMPLETED_WAITING_FOR_24H_RECALL_WINDOW
participant_target: 3_to_8
privacy_mode: anonymized_only
real_session_started: true
real_session_reported: true
report_source: facilitator_user_attestation
```

> 本账本只记录真实发生。未发生的字段保持 `NOT_OBSERVED`，禁止补写、推演或使用 AI Persona 替代真人证据。

## 0. Session

```yaml
session_id: 20260818-small-class-v1
session_date: 2026-08-18
scheduled_start: NOT_OBSERVED
actual_start: NOT_OBSERVED
actual_end: NOT_OBSERVED
reported_total_duration_min: 120
format: small_class
facilitator: RAY
participant_count: 5
source_pr_head_at_authorization: c9aedb03c636f66402456c75e74198ca7689388d
protocol_frozen: true
```

已确认的现场事实：

- 真人小班授课已发生；
- 参与人数：5 人；
- 课程总时长：约 120 分钟；
- 讲师报告：学员对本轮新概念整体反馈积极、认可度高。

证据边界：

```text
positive_reaction = observed_by_facilitator
positive_reaction ≠ 24h_recall
positive_reaction ≠ concept_boundary_pass
positive_reaction ≠ behavior_change
positive_reaction ≠ reusable / compounding
```

由于尚未记录准确或近似 `actual_end`，24h Recall 的时间窗暂不能精确冻结。

## 1. Participant Registry

仅使用匿名编号，不写姓名、手机号、微信、公司全称、付款或其他 PII。

| pid | eligibility_confirmed | attended | full_session | 24h_recall_due | notes |
|---|---|---|---|---|---|
| P01 | NOT_OBSERVED | YES | NOT_OBSERVED | PENDING_END_TIME | 真人参与 |
| P02 | NOT_OBSERVED | YES | NOT_OBSERVED | PENDING_END_TIME | 真人参与 |
| P03 | NOT_OBSERVED | YES | NOT_OBSERVED | PENDING_END_TIME | 真人参与 |
| P04 | NOT_OBSERVED | YES | NOT_OBSERVED | PENDING_END_TIME | 真人参与 |
| P05 | NOT_OBSERVED | YES | NOT_OBSERVED | PENDING_END_TIME | 真人参与 |
| P06 | N/A | NO | N/A | N/A | 未使用 |
| P07 | N/A | NO | N/A | N/A | 未使用 |
| P08 | N/A | NO | N/A | N/A | 未使用 |

## 2. Per-learner live evidence

每位真人只记录最小必要证据。当前只有 session-level 用户见证，未收到逐学员闭卷记录，因此以下字段保持 `NOT_OBSERVED`。

### P01–P05

```yaml
actual_duration_min: NOT_OBSERVED
artifact_duration_min: NOT_OBSERVED
value_thread_id: NOT_OBSERVED
same_object_across_lessons: NOT_OBSERVED
one_idea_recall: NOT_OBSERVED
next_crisis_pull: NOT_OBSERVED
p0_confusion_count: NOT_OBSERVED
l03_asset_boundary: NOT_OBSERVED
l04_time_entropy_recall: NOT_OBSERVED
continuity_adaptation_boundary: NOT_OBSERVED
c1_c4_state_mapping: NOT_OBSERVED
retrieval_not_reuse_boundary: NOT_OBSERVED
state_transition_completed: NOT_OBSERVED
behavior_change_signal_live: NOT_OBSERVED
```

Session-level qualitative observation：

> 学员整体认可本轮新概念，现场反馈积极。

该观察仅作为 `immediate_reaction_signal`，不得代替逐学员认知、24h Recall 或真实行为证据。

## 3. Session-level settlement

```yaml
participant_count: 5
reported_total_duration_min: 120
immediate_reaction_signal: POSITIVE
immediate_reaction_evidence_class: facilitator_user_attestation
timing_pass_rate: NOT_OBSERVED
artifact_minimum_completion_rate: NOT_OBSERVED
value_thread_continuity_rate: NOT_OBSERVED
p0_confusion_total: NOT_OBSERVED
next_crisis_pull_rate: NOT_OBSERVED
l04_time_not_equal_compounding_recall_rate: NOT_OBSERVED
continuity_adaptation_boundary_rate: NOT_OBSERVED
c1_c4_state_mapping_rate: NOT_OBSERVED
retrieval_not_reuse_confusion_count: NOT_OBSERVED
state_transition_completion_rate: NOT_OBSERVED
```

## 4. Immediate verdict

只允许：

```text
LIVE_NOT_RUN
LIVE_IN_PROGRESS
LIVE_COMPLETED_WAITING_24H_RECALL
FAIL_SAFE
```

当前：

```yaml
live_verdict: LIVE_COMPLETED_WAITING_24H_RECALL
```

但由于 `actual_end` 尚未记录：

```yaml
24h_recall_window_state: WAITING_FOR_END_TIME
```

不得在 24h Recall 和 Evidence Settlement 前宣称 PASS / reusable / compounding / promotion。