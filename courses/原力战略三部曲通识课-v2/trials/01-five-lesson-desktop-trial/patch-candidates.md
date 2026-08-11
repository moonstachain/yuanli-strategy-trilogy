# Patch Candidates｜课程修订候选队列

> 当前状态：HUMAN_APPROVED / APPLIED / ROUND_3_REGRESSION_PASS

## Human Gate

```yaml
human_approval: true
approval_scope:
  required_P0: [PATCH-P0-01, PATCH-P0-02]
  required_P1: [PATCH-P1-01, PATCH-P1-02, PATCH-P1-03, PATCH-P1-04]
  selected_P2: [PATCH-P2-01, PATCH-P2-03]
  absorbed_boundary_line: [PATCH-P2-02]
  watch_not_applied: [W-01]
patched_snapshot_commit: e05450f800b47ff0360c75cb73365e2011d7ee69
round_3_persona: P06
round_3_result: PASS
```

该 snapshot 是Round 3唯一课程输入；Round 3期间课程正文未修改。

---

## Final Patch Queue

| Patch ID | Severity | Lesson | 原问题 | 实际应用 | Round 3 Regression | Final Decision |
|---|---|---|---|---|---|---|
| **PATCH-P0-01** | **P0** | L03 | 母体→核心竞争力 | Generator≠Capability；三种不同表型；能力清单判别；同步工具/Deck | Persona F + isolated recall 均不复发 | **APPLIED / PASS** |
| **PATCH-P0-02** | **P0** | L02 | 品类→定位词 | 强制旧/新分类与比较对象；名字最后可选；同步工具/Deck | Persona F + isolated recall 均不复发 | **APPLIED / PASS** |
| **PATCH-P1-01** | **P1** | L03 | 九格工具最后集中爆发 | A1/A2/A3/A4随课分段填写 | L3 / 15min，反证保留 | **APPLIED / PASS_AT_LIMIT** |
| **PATCH-P1-02** | **P1** | L04 | OS工具最后4分钟集中填写 | C1/C2/C3/C4边学边建；最后只做Learning/Reuse | L3 / 14min，Outcome+Reuse保留 | **APPLIED / PASS** |
| **PATCH-P1-03** | **P1** | L02 | 第二套专业口诀截流L02→L03 | 专业栈降为讲师辅助层 | Persona F自然追问“为什么偏偏是我” | **APPLIED / PASS** |
| **PATCH-P1-04** | **P1** | L04 | 二级框架抢C1—C4主记忆 | 二级框架降为局部判别标签 | 无连续Red；C1—C4闭卷可重建 | **APPLIED / PASS** |
| **PATCH-P2-01** | P2 | L05 | 工具轻度超时 | 2036回望改课后延伸 | L3 / 13min | **APPLIED / PASS** |
| **PATCH-P2-02** | P2 | L05 | “生”可能重定义母体 | 仅吸收一句边界 | Persona F未压成能力/使命标签 | **ABSORBED / PASS** |
| **PATCH-P2-03** | P2 | L05 | 五环→可补偿KPI | “守”为不可补偿约束 + 10倍收益测试 | Persona F主动拒绝总分补偿逻辑 | **APPLIED / PASS** |

---

## Watch Item

### W-01｜L01 “只有你才能发现”前台绝对化

本轮未修改L01。

Round 3结果：

> Persona F 自发理解为“更可能、更早、反复看见 + 必须被现实验证”，没有压成排他天命。

```yaml
W_01: WATCH_NOT_APPLIED
round_3_result: PASS_NOT_DESTINY
live_trial_watch: true
```

---

## Patch Application + Regression Audit

```yaml
course_snapshot_before_patch: 6be729bf56759604f2ce2ff19e5163e2206ae2cf
patch_decision_base: a26085bf1e83d3bbb6a4e46ac30ea828f034ebe7
patched_snapshot_commit: e05450f800b47ff0360c75cb73365e2011d7ee69
required_P0_applied: 2_of_2
required_P1_applied: 4_of_4
selected_P2_applied: 2_of_2
P2_boundary_absorbed: 1_of_1
watch_items_modified: 0
lesson_01_modified: false
round_3_sessions: 5_of_5
round_3_teacher_rescue: 0
round_3_result: PASS
```

## Final Patch Verdict

> **所有经Human Gate批准的Patch都已应用并在全新Persona F上完成回归。两个历史P0均未复发；结构性P1均通过。**

仍需保留的真人Live Trial观察项：

1. L03真实课堂15分钟是否足够；
2. 真人专家IP是否仍把品类压回定位词；
3. 真人务实经营者是否仍把母体压回核心竞争力；
4. L04真人填写是否保住Outcome+Reuse；
5. W-01是否在真人口语记忆中变成排他天命。
