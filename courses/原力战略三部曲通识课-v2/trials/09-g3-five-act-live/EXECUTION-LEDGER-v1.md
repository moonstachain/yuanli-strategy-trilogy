# G3 Trial 09｜真人试讲执行账本 v1

```yaml
trial_id: YL-TRILOGY-GENERAL-v2-TRIAL-09-G3-LIVE
issue: moonstachain/yuanli-strategy-trilogy#19
status: AUTHORIZED_WAITING_FOR_REAL_SESSION
participant_target: 3_to_8
privacy_mode: anonymized_only
real_session_started: false
```

> 本账本只记录真实发生。未发生的字段保持 `NOT_OBSERVED`，禁止补写、推演或使用 AI Persona 替代真人证据。

## 0. Session

```yaml
session_id: ______
scheduled_start: ______
actual_start: NOT_OBSERVED
actual_end: NOT_OBSERVED
format: ______
facilitator: ______
participant_count: 0
source_pr_head: ______
protocol_frozen: true
```

## 1. Participant Registry

仅使用匿名编号，不写姓名、手机号、微信、公司全称、付款或其他 PII。

| pid | eligibility_confirmed | attended | full_session | 24h_recall_due | notes |
|---|---|---|---|---|---|
| P01 |  |  |  |  |  |
| P02 |  |  |  |  |  |
| P03 |  |  |  |  |  |
| P04 |  |  |  |  |  |
| P05 |  |  |  |  |  |
| P06 |  |  |  |  |  |
| P07 |  |  |  |  |  |
| P08 |  |  |  |  |  |

## 2. Per-learner live evidence

每位真人只记录最小必要证据。

### P__

```yaml
pid: P__
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

原话摘要（必要时去标识化）：

- One Idea：______
- L03→L04 自然追问：______
- 最大混淆：______
- 自己的 State Transition：______

## 3. Session-level settlement

```yaml
participant_count: NOT_OBSERVED
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
live_verdict: LIVE_NOT_RUN
```

不得在 24h Recall 和 Evidence Settlement 前宣称 PASS / reusable / compounding / promotion。