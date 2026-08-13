# Five-Lesson Anchor-Cut Live Trial

> 状态：`READY_NOT_RUN`

```yaml
trial_id: YL-TRILOGY-GENERAL-v2-ANCHOR-LIVE-001
scope: L01_to_L05_anchor_cuts
anchor_count: 10
status: READY_NOT_RUN
requires_real_learners: true
synthetic_trial_not_sufficient: true
```

## 目标

验证“故事、硬史料、高弧光、跨学科纵深”是否真的提升：

- 注意力；
- 概念理解；
- 24h 记忆；
- 迁移；
- PERSONAL_VERDICT 质量；
- 工具完成质量。

而不是只让课堂更好听。

## 每课只验证两个 Anchor

```text
L01｜Gutenberg + Deep Blue
L02｜Nokia/iPhone + Wii
L03｜John Snow + Tu Youyou
L04｜Model 299 + Toyota
L05｜Washington + Patagonia
```

试讲期间禁止增加第三个旗舰故事。

## 每个 Anchor 采集

```yaml
scene_recall_24h: not_run
anomaly_recall_24h: not_run
dilemma_authenticity: unknown
evidence_trust: unknown
arc_recall_24h: not_run
fact_interpret_separation: not_run
concept_reveal_timing: unknown
mechanism_transfer: not_run
personal_verdict_quality: not_run
story_overpowers_concept: unknown
```

## 课程级采集

```yaml
L01_to_L02_pull: not_run
L02_to_L03_pull: not_run
L03_to_L04_pull: not_run
L04_to_L05_pull: not_run
five_course_story_reconstruction: not_run
tool_completion_quality: not_run
```

## PASS 条件

至少满足：

1. 24h 后学员能用故事复原“判断”，而不只是人物名；
2. 能区分“史料事实”和“原力解释”；
3. 能迁移到一个课堂没讲过的业务情境；
4. 每课至少一个 `PERSONAL_VERDICT` 具有真实代价或可观察行动；
5. 故事没有挤压唯一工具和唯一产物；
6. 课尾悬念仍自然指向下一课。

## FAIL / PATCH 信号

- 只记住人物和数字；
- 学员开始讨论历史细节，却忘了自己；
- 把案例成功等同于模型必然正确；
- 跨学科部分成为第二堂知识课；
- 概念出现太晚导致迷失，或太早导致故事沦为例子；
- 工具时间被故事吃掉；
- 第五课只感动，没有真实 No。

## 法权

本目录只定义真人试讲协议，不宣称试讲已经发生。
