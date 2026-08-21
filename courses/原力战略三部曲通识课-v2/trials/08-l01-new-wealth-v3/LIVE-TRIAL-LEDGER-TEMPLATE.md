# L01 V3.1｜真人试讲 Evidence Ledger Template

```yaml
candidate: YL-TRILOGY-GENERAL-v2-L01-V3.1-CANDIDATE
snapshot_sha: eda55d3d653c03ba2c3b78822745e80f1b9b10f3
evidence_class: real_learner_trial
status: TEMPLATE_NOT_RUN
```

## Session Metadata

```yaml
date:
teacher:
learner_count:
learner_profile:
start_time:
end_time:
actual_duration_min:
course_snapshot_verified: false
```

## 1｜Timing Ledger

| Segment | Planned | Actual | Over/Under | Notes |
|---|---:|---:|---:|---|
| 00—07 冷开场 | 7 | | | |
| 07—15 能 | 8 | | | |
| 15—26 贵 | 11 | | | |
| 26—36 值 | 10 | | | |
| 36—46 我 | 10 | | | |
| 46—56 秘密 | 10 | | | |
| 56—63 杠杆 | 7 | | | |
| 63—68 时间 | 5 | | | |
| 68—80 Live Core | 12 | | | |
| 80—84 公式 | 4 | | | |
| 84—87 地图 | 3 | | | |
| 87—90 Recall/Handoff | 3 | | | |

## 2｜即时 Recall

每位学员闭卷写：

```text
能 =
贵 =
值 =
我 =
```

汇总：

```yaml
full_reconstruction_rate:
partial_rate:
fail_rate:
```

## 3｜秘密误解

固定题：

> “一个很好的 AI 商业机会，是不是就等于你的秘密？”

```yaml
correct_opportunity_secret_boundary_rate:
critical_misconception_count:
representative_wrong_answers:
```

## 4｜Artifact

```yaml
completion_rate:
value_candidate_completion_rate:
L3_rate:
median_completion_time_min:
p90_completion_time_min:
```

常见阻塞：

- [ ] 抽象人格标签
- [ ] 赛道/风口替代秘密
- [ ] 不知道真实人群/问题
- [ ] D 区没有可保留物
- [ ] Value Candidate 使命化
- [ ] 其他：

## 5｜Cognitive Load

```yaml
highest_load_segment:
low_count:
medium_count:
high_count:
teacher_rescue_required:
```

## 6｜L02 Handoff

固定问：

> “你现在最想继续解决的下一个问题是什么？”

逐字记录第一自发问题，再分类：

```yaml
L02_market_payment_category_scaling_moat:
L03_mother_source:
L05_life_mission:
in_lesson_detail:
other:
```

## 7｜24h Recall Queue

试讲后约 24h 执行，不提前给题目材料。

```yaml
scheduled_for:
executed_at:
response_rate:
```

六问见 `LIVE-TRIAL-AUTHORIZATION.md`。

## 8｜Live Verdict

只能在真实数据填写后选择：

```yaml
live_verdict:
  - PASS_TO_24H_RECALL
  - REVISE_BEFORE_RECALL_DECISION
  - FAIL
validated_live: false
promotion: NOT_AUTHORIZED
```
