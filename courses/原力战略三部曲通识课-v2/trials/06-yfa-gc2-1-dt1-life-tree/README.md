# YFA-GC2.1-DT1｜L03 Force Asset Life-Tree Desktop Trial

> Blind Learner × Observer × Examiner × Red Team

```yaml
trial_id: YFA-GC2.1-DT1
lesson: YL-TRILOGY-GENERAL-v2-L03
evidence_class: simulated_desktop_trial
real_learner_evidence: false
canon_effect: none
pr: 25
round_1: COMPLETE
patch_application: COMPLETE
round_2_regression: COMPLETE
status: DESKTOP_TRIAL_PASS_SIMULATED_WITH_CONDITIONS
qualification: READY_FOR_SMALL_SAMPLE_LIVE_TRIAL_NOT_RUN
reusable: false
supersedes_existing_l03: false
```

# 一、基准方法

DT1 按 Soul 教学正典 `YUANLI-CONCEPT-LESSON-CARD-STANDARD-v1` 检查：

```text
一课一念
一念三幕
一课一果
↓
小切口
大纵深
高弧光
强落地
迁移验证
递归回写
```

90 分钟额外 30 分钟必须用于案例讨论、填写、互评、讲师反馈与修改，不允许继续堆知识。

本轮只验证教学编译，不验证 Mother / Force / Asset 的现实真实性。

---

# 二、Round 1｜Pre-Patch Blind Desktop Run

输入：PR #25 初始 v2.1 director + deck + exercise。

结论：

```yaml
result: FAIL_WITH_ACTIONABLE_EVIDENCE
critical_misconception: 0
canon_boundary_breach: 0
teaching_runtime_blockers: 2
p1_load_issues: 2
```

## BLOCKER-01｜小切口出现太晚

初始版本：

```text
0—8  职业 / 能力剥离
8—14 荣格深层形成链
14—18 Self
18—36 John Snow
```

问题：教学正典要求前 5—7 分钟出现“具体的人、时刻、两难、代价、旧解释破裂”。初版前 18 分钟仍以抽象剥离与概念为主。

裁决：`FAIL_SMALL_CUT_GATE`。

## BLOCKER-02｜一课一果现场不可完成

初始《原力资产生成树》要求课堂同时完成：

- Formation Lens；
- Self-Endorsed Direction；
- Mother 四窗口；
- 三表型；
- 反证与竞争解释；
- Force Thesis 五变量；
- Force 四 Gate；
- 90-Day World Validation；
- Preserve / Retrieve / Task2 / Lift；
- 闭卷整合。

它是一份优秀的 90 天研究工作簿，但不是 90 分钟的一课一果。

裁决：`FAIL_ARTIFACT_TIME_GATE`。

## P1-01｜荣格术语负荷过高

6 分钟内同时出现：

```text
Archetype
Complex
Shadow
Persona
Ego
Individuation
Self
```

风险：学员记住“荣格名词”，而不是 `Self → Mother` 的法权边界。

## P1-02｜后台科学术语过早占据前台

`Force Thesis / Baseline / Predicted Delta / Validated Force / Atomic Force Asset` 都是必要后台概念，但在 90 分钟通识课中同时要求学员掌握，会稀释“一棵树”的主记忆。

---

# 三、Patch Set｜已应用

## PATCH-P0-01｜Anchor 前移

John Snow 从 18 分钟前移到 **第 3 分钟**。

新顺序：

```text
0—3  学员职业 / 能力剥离
3—13 John Snow 具体小切口
13—18 生命树与 Self / Mother 边界
```

结果：小切口在前 7 分钟已经出现具体人物、具体时刻、真实两难与现实代价。

## PATCH-P0-02｜工具拆成“课堂六格 + 课后扩展”

课堂只完成：

```text
1 根｜Mother Hypothesis + 反证
2 归｜Self-Endorsed Direction + 真实拒绝
3 主干｜原力下注
4 炼｜一条判断规则
5 果实｜90-Day World Test
6 种子｜Preserve + Task2 + Lift
```

详细 Formation Lens、Force 四 Gate、Attribution、Baseline 等移入课后 90 天扩展协议。

## PATCH-P1-01｜荣格术语退居讲师备注

前台只讲：

```text
共同心理可能性
× 个人生命史
× 适应 / 冲突
→ Self
```

Archetype / Complex / Shadow / Persona / Individuation 继续保留为解释来源，但不作为课堂必记术语。

## PATCH-P1-02｜科学术语前后台分层

前台：

```text
原力下注
果实
种子
```

后台：

```text
Force Thesis
Validated Force
Atomic Force Asset
```

不牺牲治理边界，但降低通识课认知负荷。

## PATCH-P1-03｜90 分钟时间预算重排

```yaml
teacher_explanation_and_anchors: 54min
learner_write_peer_review_transfer: 36min
```

新增的学习时间被用于填写、互评、修改和迁移，没有继续堆知识。

---

# 四、Round 2｜Post-Patch Regression

使用修补后的 director v2.2-DT1、deck v2.2-DT1、exercise v1.1-DT1 做模拟回归。

## Persona A｜方法很多型专家

高风险错误：

> “我的 Mother 就是战略 / 结构化。”

当前防线：

1. 三个不同表型；
2. 岗位 JD 判别；
3. 一个反证；
4. 同伴互评。

裁决：`PASS_SIMULATED`。

## Persona B｜成熟经营型企业家

高风险错误：

> “这套解释很准，但不改变现实资源配置。”

当前防线：

> “即使赚钱，我也不愿长期成为 / 持续做 ______。”

必须填写真实角色、项目或工作方式。

裁决：`PASS_SIMULATED`。

## Persona C｜AI 工具狂热者

高风险错误：

> “AI 帮我做出来了，所以这就是我的 Force / Asset。”

当前防线：

```text
AI-assisted Performance ≠ Human Capability Growth
一次结果 ≠ Asset
留下笔记 ≠ Reuse
```

并要求 materially distinct Task2。

裁决：`PASS_SIMULATED`。

---

# 五、质量闸门回归

| Gate | Pre-Patch | Post-Patch DT1 | 裁决 |
|---|---|---|---|
| 一课一念 | PASS | PASS | KEEP |
| 一个核心模型 | PASS | PASS | 生命树唯一母图 |
| 一个最终产物 | PARTIAL | PASS_SIMULATED | 六格主卡 |
| 前7分钟小切口 | FAIL | PASS | John Snow @ min3 |
| 具体人/时刻/两难/代价 | FAIL_EARLY | PASS | Anchor 压缩 |
| 大纵深 | PASS | PASS | Self→Mother→Force→Asset |
| 高弧光有真实取舍 | PASS | PASS | 舍弃不属于自己的成功 |
| 反证可见 | PASS | PASS | Mother 必填一个反证 |
| 90min 非知识堆积 | FAIL | PASS_BY_DESIGN | 36min active work |
| Generator ≠ Capability | PASS | PASS | 三表型 + JD 判别 |
| Mother ≠ Force | PASS | PASS | 保留 |
| Force ≠ Asset | PASS | PASS | 果实≠种子 |
| Task2 Reuse | PASS_CONCEPT | PASS_CONTRACT | 真实发生待90天 |
| L03→L04 Handoff | PASS | PASS | 种子若仍只在本人→OS |
| Canon boundary | PASS | PASS | canon_effect none |

---

# 六、DT1 最终裁决

```yaml
desktop_trial: PASS_SIMULATED_WITH_CONDITIONS
structural_blockers_remaining: 0
critical_misconceptions_in_simulation: 0
real_learner_evidence: false
real_90min_timing: NOT_PROVEN
real_24h_recall: NOT_RUN
real_7d_transfer: NOT_RUN
real_90d_task2_reuse: NOT_RUN
reusable: false
canon_candidate: false
```

DT1 证明的是：

> **修补后的 L03 已经达到“值得真人试讲”的桌面结构资格。**

DT1 不证明：

- 真人能在 90 分钟完成六格；
- 真人不会把 Mother 压回能力标签；
- 24h 后仍记得生命树；
- Force Thesis 对普通学员一定不增加负担；
- 90 天世界验证会成功；
- Task2 reuse 会真实发生。

---

# 七、下一 Gate

正式进入：

# **YFA-GC2.1-LT1｜Small-Sample Human Live Trial**

建议只观察 6 个变量：

```yaml
live_completion:
  - classroom_six_field_tree_completion_time
recall_24h:
  - life_tree_spine
  - self_not_mother
  - mother_not_force
  - force_not_asset
misconception:
  - mother_collapses_to_capability
  - jung_terms_capture_attention
personal_verdict:
  - real_opportunity_cost_written
transfer:
  - force_bet_applied_to_unseen_problem
assetization:
  - task2_is_materially_distinct
```

在 Live Trial 前，不再加第三案例、不增加新概念、不继续扩展工具字段。
