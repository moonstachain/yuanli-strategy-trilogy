# Patch Candidates｜课程修订候选队列

> 当前状态：HUMAN_APPROVED / APPLIED_FOR_ROUND_3

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
```

该 snapshot 冻结的是本轮修订后的课程输入：L02—L05授课稿、对应主工具与Deck蓝图。Round 3 必须只读取该 commit，不得读取之后的治理写回。

---

## Patch Queue

| Patch ID | Severity | Lesson | 原问题 | 实际应用 | Regression Target | Decision |
|---|---|---|---|---|---|---|
| **PATCH-P0-01** | **P0** | L03 | 母体被稳定压缩成“底层核心竞争力/核心能力” | 增加 `Generator != Capability` 强判别；同一生成机制必须解释至少三种不同能力/职业载体；新增能力清单/JD判别；同步修改母体卡与Deck | Persona F 必须区分 `generator != capability`；不能把母体压成核心竞争力 | **APPLIED / REQUIRED_REGRESSION** |
| **PATCH-P0-02** | **P0** | L02 | 品类被稳定压缩成“定位词/超级标签” | 工具强制填写 `旧分类/旧比较对象 → 新分类/新比较对象`；名字改为可空最后一步；新增两组正反例与闭卷判别；同步修改Deck | Persona F 必须解释好名字≠新品类；必须能说明分类/比较框架变化 | **APPLIED / REQUIRED_REGRESSION** |
| **PATCH-P1-01** | **P1** | L03 | 九格母体卡最后9分钟，3/3 Persona无法达到L3 | A1填1—6、A2填7、A3填8、A4填9；78—87只整合与判别 | Persona F L03等价工作量≤15min且L3；反证不得为空 | **APPLIED / REQUIRED_REGRESSION** |
| **PATCH-P1-02** | **P1** | L04 | OS一页架构最后4分钟集中填写 | 开场填单点故障；C1/C2/C3/C4后分别填写对应格；84—88只完成Learning/Reuse与闭环检查 | Persona F L04≤15min且含Outcome+Reuse | **APPLIED / REQUIRED_REGRESSION** |
| **PATCH-P1-03** | **P1** | L02 | “一势两账三链四权”截流，L2→L3 Handoff失败 | 该专业栈降为讲师辅助层；学生主记忆只保留“见名繁守+四财富”；Deck同步取消第二套口诀 | Persona F L02结束自然问题指向“为什么偏偏是我” | **APPLIED / REQUIRED_REGRESSION** |
| **PATCH-P1-04** | **P1** | L04 | 二级框架与C1—C4竞争工作记忆 | C1—C4母图常驻；Cited/Inferred/Unknown、能力类型、现实链全部降为局部判别标签；闭卷只考原则/证据/押注/执行/回写 | Persona F L04无连续Red；仍能拒绝OS=工具栈 | **APPLIED / REQUIRED_REGRESSION** |
| **PATCH-P2-01** | P2 | L05 | 工具轻度超时 | 2036回望改为课后延伸，不计课堂Green Gate；五格核心不删 | Persona F L05≤14min且保留真实tradeoff | **APPLIED / SELECTED** |
| **PATCH-P2-02** | P2 | L05 | “生”可能被写成核心能力或品牌使命 | 只吸收一句边界：“第三课问生成源是什么；第五课不重新定义母体，只问希望它长期生成什么。” | Persona F `生`不等于能力/使命标签 | **ABSORBED_MINIMAL_LINE** |
| **PATCH-P2-03** | P2 | L05 | 高成就Persona把五环做成五维KPI | 明确“守”是不可被其他高分补偿的约束；增加10倍收益压力测试；Deck/工具同步 | Persona F能说明价值约束≠KPI权重 | **APPLIED / SELECTED** |

---

## Watch Items

### W-01｜L01 “只有你才能发现”前台绝对化

Round 2 可被现有“更可能先看见 + 可验证”边界纠正，因此本轮未改L01。

Round 3继续观察：

> Persona F 是否自然理解为“更可能持续看见/生成的差异”，而不是排他天命。

状态：`WATCH_NOT_APPLIED`。

---

## Patch Application Audit

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
patch_application_status: COMPLETE
```

受影响课程文件：

```text
lessons/02-原力创业-找到秘密.md
lessons/03-原力资产-为什么偏偏是你.md
lessons/04-原力OS-让原力离开你仍然生长.md
lessons/05-原力人生-什么值得被复制一万倍.md

exercises/我的原力秘密四步卡-v1.md
exercises/我的原力母体假设卡-v1.md
exercises/我的原力OS一页架构-v1.md
exercises/我的原力人生一页纸-v1.md

deck/02-原力创业-PPT蓝图.md
deck/03-原力资产-PPT蓝图.md
deck/04-原力OS-PPT蓝图.md
deck/05-原力人生-PPT蓝图.md
```

L01及其工具/Deck未修改。

---

## 下一 Gate

```text
patched snapshot frozen
→ create brand-new Persona F
→ Round 3 Regression: F runs L01→L05
```

Round 3 不得使用 P01—P05 证明修复有效；不得读取 Round 1/2 的学员答案、Patch Queue 或 Red Team 结论作为 Learner 上下文。
