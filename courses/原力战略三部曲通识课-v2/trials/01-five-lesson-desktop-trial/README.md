# 原力战略五课 Desktop Trial v1

> Blind Learner × Observer × Examiner × Red Team

## 当前裁决

```yaml
trial_id: YL-TRILOGY-GENERAL-v2-DESKTOP-01
original_input_snapshot: 6be729bf56759604f2ce2ff19e5163e2206ae2cf
patched_input_snapshot: e05450f800b47ff0360c75cb73365e2011d7ee69
evidence_class: simulated_desktop_trial
real_learner_evidence: false
status: PATCHED_SNAPSHOT_FROZEN
qualification: NOT_YET_QUALIFIED_FOR_LIVE_TRIAL
round_1: COMPLETE
round_2: COMPLETE
patch_application: COMPLETE
round_3: READY_NOT_RUN
next_gate: ROUND_3_REGRESSION
```

---

# 已完成的测试

## Round 1｜Blind Run

```text
P01 方法很多型专家
P02 成熟经营型企业家
P03 专家IP型创业者
× L01—L05
= 15/15纵向Session
```

结论：`FAIL_WITH_ACTIONABLE_EVIDENCE`。

主要发现：

1. L03：母体被压成“底层核心竞争力”；
2. L02：品类被压成“定位词/超级标签”；
3. L03工具3/3无法在课堂时间窗达到L3；
4. L04工具3/3无法在课堂时间窗达到L3；
5. P01 L02→L03被第二套专业口诀截流。

详见：`ROUND-1-REVIEW.md`。

## Round 2｜Adversarial Run

```text
P04 AI工具狂热者 × L04
P05 高成就效率主义者 × L05
+ 29个Red Team横向攻击
```

结论：`CONFIRMS_ROUND_1_BLOCKERS`。

- 两个Round 1 P0再次被对抗条件重复击穿；
- 没有新增Critical Misconception；
- 正典硬边界全部守住；
- L04中段负荷与工具时间再次被P04确认；
- L05“人生=五维KPI”可被交换测试纠正，但存在轻度摩擦。

详见：

- `ROUND-2-REVIEW.md`
- `red-team/ROUND-2-ADVERSARIAL-BATTERY.md`

---

# Human Gate｜Patch 已批准并应用

Human批准范围：

```yaml
P0: 2_of_2
P1: 4_of_4
selected_P2:
  - PATCH-P2-01
  - PATCH-P2-03
absorbed_boundary_line:
  - PATCH-P2-02
watch_not_applied:
  - W-01
```

## 应用后的核心变化

### L02｜品类 ≠ 定位词

现在工具必须先完成：

```text
旧分类 / 旧比较对象
→ 新分类 / 新比较对象
→ 名字最后可选
```

如果只换了一个更好记的词，分类与比较没有改变，不通过B2。

同时，“一势两账三链四权”降为讲师辅助层；学生主记忆只保留：

> **见 · 名 · 繁 · 守 + 四种财富。**

### L03｜Generator ≠ Capability

现在 Mother Hypothesis 必须证明：

> **同一个生成机制至少能长出三种不同能力 / 职业 / 作品载体。**

如果一句话仍可直接写进核心能力清单或岗位JD，不能自动当作母体。

母体卡改成：

```text
A1填1—6
A2填7
A3填8
A4填9
课末只整合与判别
```

### L04｜边学边建OS

工具改成：

```text
开场 → 单点故障
C1后 → 原则 / Human Gate
C2后 → 事实 / 证据 / Unknown
C3后 → Top1 / Stop
C4后 → Owner / Action / Evidence / Outcome
最后 → Learning / Reuse
```

Cited/Inferred/Unknown、三类能力、现实链全部降为局部标签，不再和C1—C4竞争主记忆。

### L05｜价值约束 ≠ 五维KPI

- “守”明确为不可被其他高分补偿的约束；
- 增加10倍收益压力测试；
- 增加一句：“第三课问生成源是什么；第五课不重新定义母体，只问希望它长期生成什么”；
- 2036回望改为课后延伸，不计课堂核心Green Gate。

---

# Patched Snapshot｜已冻结

Round 3唯一课程输入：

```text
e05450f800b47ff0360c75cb73365e2011d7ee69
```

该 commit 冻结了本轮受影响的课程稿、主工具与Deck蓝图；之后的Trial治理写回不得改变Round 3输入。

详见：`PATCH-APPLICATION-RECEIPT.yaml`。

---

# Round 3｜Regression Run｜READY_NOT_RUN

全新 Persona：

> `personas/P06-regression-founder.yaml`

别名：`Persona F`。

Persona F 被明确禁止读取：

- Round 1/2 Session；
- Red Team答案；
- Patch Queue；
- Patch ID；
- Soul正典与项目记忆；
- 未来课程内容。

Round 3 必须：

```text
Persona F
L01 → L02 → L03 → L04 → L05
```

并重新检查：

1. 品类是否仍会压成定位词；
2. 母体是否仍会压成核心竞争力；
3. L02→L03 Handoff是否恢复；
4. L03工具是否≤15min等价工作量且L3；
5. L04是否无连续Red窗口；
6. L04工具是否≤15min且有Outcome+Reuse；
7. L05是否理解价值约束≠KPI；
8. L05工具是否≤14min且L3；
9. L01“只有你”是否仍被误解为排他天命；
10. 五课结束能否闭卷重建完整龙骨。

---

# 正典硬边界｜仍不变

```yaml
A_B_C_canon_order: A_to_B_to_C
B4_barriers: [虚, 实, 入, 出]
C5_exists: false
yuanli_life_is_fourth_part: false
human_gate_required: true
```

本次Patch修的是教学判别、负荷与工具编排，不修改Soul正典。

---

# 证据目录

```text
ROUND-1-REVIEW.md
ROUND-2-REVIEW.md
PATCH-APPLICATION-RECEIPT.yaml
protocol.md
DESKTOP-TRIAL-RECEIPT.yaml

personas/
  P01—P06

sessions/
  Round1 + Round2 evidence

red-team/
  ROUND-2-ADVERSARIAL-BATTERY.md

ledgers/
  misconception-ledger.md
  cognitive-load-ledger.md
  tool-completion-ledger.md
  narrative-handoff-ledger.md

cross-course/
  Round1 reconstructions + recall proxies

patch-candidates.md
```

---

# 当前唯一允许动作

> **RUN_ROUND_3_PERSONA_F_L01_TO_L05_AGAINST_PATCHED_SNAPSHOT**

在Round 3完成前：

- 不继续修改 patched course snapshot；
- 不用P01—P05证明修复有效；
- 不宣称Desktop Trial PASS；
- 不宣称Live Trial Ready；
- 不宣称reusable；
- 不宣称supersedes v1。
