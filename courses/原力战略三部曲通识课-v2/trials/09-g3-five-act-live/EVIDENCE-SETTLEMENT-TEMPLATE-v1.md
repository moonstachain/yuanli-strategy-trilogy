# G3 Trial 09｜Evidence Settlement Template v1

```yaml
trial_id: YL-TRILOGY-GENERAL-v2-TRIAL-09-G3-LIVE
status: BLOCKED_UNTIL_REAL_LIVE_AND_24H_EVIDENCE
fresh_human_gate_required: true
promotion_default: blocked
```

> 本文件只能在真实 Live Session、24h Recall 与 Behavior Change Evidence 完成后填写最终值。缺失项保持 `NOT_OBSERVED`，不得用 Desktop / AI 模拟补齐。

## 1. Evidence completeness

```yaml
real_participant_count: NOT_OBSERVED
min_3_real_participants_met: NOT_OBSERVED
live_timing_complete: NOT_OBSERVED
concept_confusion_complete: NOT_OBSERVED
artifact_chain_complete: NOT_OBSERVED
24h_recall_complete: NOT_OBSERVED
behavior_change_review_complete: NOT_OBSERVED
privacy_check: NOT_OBSERVED
```

任一关键项缺失：`STOP / INCOMPLETE_EVIDENCE`。

## 2. Frozen hypotheses

### H1｜五幕可记忆
`重估 → 入世 → 留存 → 继承 → 定向`

### H2｜L03→L04 边界成立
`留下来 ≠ 复利`

### H3｜L04 WHY 有解释增益
学员能理解“时间不会自动产生复利”，并识别至少一种时间熵。

### H4｜Continuity × Adaptation 可理解
学员能解释仅连续会僵化、仅适应会漂移。

### H5｜C1-C4 没有被误解为四类新资产
`Normative / Epistemic / Policy / Reality` 映射通过。

### H6｜Retrieval ≠ Reuse
无 P0 混淆。

### H7｜State Transition 可落地
学员能给出真实 `Reality → Learning → next Task change`。

### H8｜课程产生现实行为变化信号
多数参与者出现至少一个可观察的 DEC / REJECT / SAVE / ACT change。

## 3. Metrics

```yaml
five_act_24h_recall_rate: NOT_OBSERVED
artifact_chainable_rate: NOT_OBSERVED
l03_min_asset_card_completion_rate: NOT_OBSERVED
l04_time_not_equal_compounding_recall_rate: NOT_OBSERVED
continuity_adaptation_boundary_rate: NOT_OBSERVED
c1_c4_state_mapping_rate: NOT_OBSERVED
retrieval_not_reuse_confusion_count: NOT_OBSERVED
state_transition_example_completion_rate: NOT_OBSERVED
participants_with_observable_behavior_change: NOT_OBSERVED
behavior_change_majority: NOT_OBSERVED
```

## 4. Qualitative failures first

按优先级记录：

```text
P0 Canon/ontology confusion
→ P0 assetization/compounding confusion
→ P0 retrieval/reuse confusion
→ P0 artifact impossible to finish
→ P1 narrative recall failure
→ P1 L03→L04 weak pull
→ P1 L04 becomes tech-stack lesson
→ P1 VALUE THREAD breaks
```

每个失败项：

```yaml
failure_id: ______
evidence_refs: ______
frequency: ______
severity: P0|P1|P2
root_cause_hypothesis: ______
minimum_patch: ______
requires_retest: true|false
```

## 5. Final machine settlement

只允许：

```text
PASS_FOR_FRESH_HUMAN_GATE
REVISE_AND_RETEST_RECOMMENDED
INCOMPLETE_EVIDENCE
FAIL_SAFE
```

```yaml
machine_settlement: INCOMPLETE_EVIDENCE
reason: real evidence not yet collected
```

## 6. Fresh Human Gate

Human 只裁决：

```text
APPROVE_PROMOTION
或
REVISE_AND_RETEST
```

Human Gate 前保持：

```yaml
pr18_merge_authorized: false
pr528_merge_authorized: false
promotion_authorized: false
reusable: false
compounding_proven: false
```