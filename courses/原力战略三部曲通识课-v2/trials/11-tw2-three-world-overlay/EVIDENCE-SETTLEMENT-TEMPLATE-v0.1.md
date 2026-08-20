# TW2 Three Worlds｜Evidence Settlement Template v0.1

> session_date: `TBD`
> cohort: `TBD`
> participants: `TBD`
> evidence_level: `L0 | L1 | L2`
> status: `NOT_RUN`

## 1. Session facts

```yaml
real_session_occurred: false
participants: null
duration_min: null
overlay_used: false
observer_present: false
l1_sample_size: 0
```

## 2. Learner evidence rows

只记录实际观察到的证据；未观察写 `NA`，不要猜。

| learner | explanation E0-E3 | navigation N0-N3 | canon_retained | M1 source=test | M2 reality=money | M3 future=AI | M4 parallel canon | M5 journey=ontology | net signal | evidence note |
|---|---|---|---|---|---|---|---|---|---|---|
| P01 | NA | NA | NA | NA | NA | NA | NA | NA | NA | |

## 3. Aggregate metrics

只对有对应证据的样本计算分母。

```yaml
correct_three_world_explanation_rate: null
self_problem_navigation_rate: null
canonical_mapping_retained: null
misconception_rate:
  M1_source_as_test: null
  M2_reality_as_money: null
  M3_future_as_ai: null
  M4_parallel_canon: null
  M5_journey_equals_ontology: null
new_parallel_canon_misread_count: null
```

## 4. Threshold comparison

目标：

```yaml
correct_three_world_explanation_rate: ">= 0.80"
core_misconception_rate_each: "< 0.20"
self_problem_navigation_rate: ">= 0.70"
canonical_mapping_retained: true
new_parallel_canon_misread_count: 0
```

结果：

```yaml
explanation_gate: NOT_EVALUATED
navigation_gate: NOT_EVALUATED
misconception_gate: NOT_EVALUATED
canon_retention_gate: NOT_EVALUATED
parallel_canon_gate: NOT_EVALUATED
```

## 5. Qualitative evidence

### Strongest evidence for keeping Three Worlds

- TBD

### Strongest evidence against keeping Three Worlds

- TBD

### Unexpected learner language

- TBD

### Where old labels still outperform Three Worlds

- TBD

## 6. Settlement

只允许以下之一：

```text
PROMOTION_CANDIDATE
REVISE_AND_RETEST
KEEP_AS_OPTIONAL_ORIENTATION
REJECT_BY_REALITY
INSUFFICIENT_EVIDENCE
```

Current:

```text
INSUFFICIENT_EVIDENCE
```

## 7. Claim boundary

在达到 Human Gate 以前，不允许把 Trial 结果写成：

- “Three Worlds 已证明更有效”；
- “Three Worlds 已成为课程标准”；
- “Three Worlds 可以全渠道推广”。

真人信号只能支持与证据等级相匹配的声明。
