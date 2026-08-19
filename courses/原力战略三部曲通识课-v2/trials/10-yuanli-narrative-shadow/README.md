# Trial 10｜原力叙事 Shadow

```yaml
trial_id: YL-TRILOGY-GENERAL-v2-TRIAL-10-NARRATIVE-SHADOW
status: READY_NOT_RUN
mode: CALIBRATION_SHADOW
stacked_on_pr: 18
stacked_on_head: 1b509fe28e1052f72ff80f93e99b527bd912c966
learner_facing_change: none
real_learners_required: true
sample_target: 3_to_8
method_source: moonstachain/yuanli-strategy-soul#541
method_human_review: recommendation_only_pending_ray
promotion_effect: none
```

> 本 Shadow 不改变 G3 五课任何学员侧输入；它只升级后台观察方式。

## 1. 冻结输入

继续使用 PR #18 当前冻结的：

```text
L01 原力战略｜重估
→ L02 原力创业｜入世
→ L03 原力资产｜留存
→ L04 原力 OS｜继承
→ L05 原力人生｜定向
```

继续使用同一 `VALUE_THREAD_ID`、当前 Director / Deck / Exercise / Cliffhanger / Timing 与 Trial 09 规则。

禁止为了 Shadow 得分修改：

- 五幕；
- 案例；
- 讲稿；
- 学员工具；
- 课堂时间；
- P0 概念测试；
- 原有 24h 问题。

## 2. 双账并行

同一批真实学员产生两套独立 Evidence：

```text
A. Course Evidence｜Trial 09
Timing / One Idea / Artifact / VALUE THREAD / P0 / Cliff / Behavior

B. Narrative Shadow Evidence｜Trial 10
八态 / 七证 / T0 / 24h / 7d / 30d
```

A/B 不互相冒充。

## 3. 原力叙事八态

后台观察：

> **唤 → 裂 → 聚 → 构 → 辨 → 生 → 迁 → 化**

第一轮不是证明八态正确，而是回答：

- 哪些状态真实可观察？
- 哪些状态重叠？
- 哪些状态对诊断课程有增量价值？
- 哪些只是漂亮理论？

每态最终允许：

`KEEP | REVISE | MERGE | DROP | UNOBSERVABLE`

## 4. 时间证据

```text
T0      课堂：Model Update
T+24h   Retrieval
T+7d    Transfer（陌生新场景）
T+30d   Reality Use / Behavior Signal
```

未发生的时间点必须 `NOT_RUN`。

## 5. 当前状态

```yaml
trial_09_course_live: AUTHORIZED_READY_NOT_RUN
trial_10_shadow: READY_NOT_RUN
real_learner_evidence: none
T0: NOT_RUN
T24h: NOT_RUN
T7d: NOT_RUN
T30d: NOT_RUN
settlement: NOT_STARTED
confirmation: NOT_STARTED
lesson_standard_v2: NOT_AUTHORIZED
machine_contract_change: NOT_AUTHORIZED
```

## 6. 法定后续

```text
3–8 人 G3 Trial 09 + Narrative Shadow
→ T0
→ 24h
→ 7d
→ 30d
→ Calibration Settlement
→ REVISE_AND_CONFIRM / KEEP_EXPLANATORY / REJECT
→ 第二轮不同学员或不同课程 Confirmation
→ Fresh Human Gate
→ 仅在现实支持时提出 Soul Lesson Standard v2
→ 再单独提出 Template / Schema / Skill / CI PR
```
