# 原力战略五课 Desktop Trial v1

> Blind Learner × Observer × Examiner × Red Team

## 目的

这不是内部审稿，也不是证明课程正确。

唯一目的：在进入真人课堂前，主动寻找五课内容中最可能导致学习失败的地方。

重点检测：

1. 哪里第一次听不懂；
2. 哪里自以为听懂但理解错；
3. 哪里新概念过多导致前面内容掉线；
4. 五张主工具是否能在目标时间内完成到可用水平；
5. 90 分钟节奏是否存在必然超载；
6. L1→L2→L3→L4→L5 是否自然产生下一课问题；
7. 五课结束后能否重建一条完整心智龙骨。

## 冻结输入

```yaml
trial_id: YL-TRILOGY-GENERAL-v2-DESKTOP-01
trial_version: v1
course_version: YL-TRILOGY-GENERAL-v2
input_snapshot_commit: 6be729bf56759604f2ce2ff19e5163e2206ae2cf
input_snapshot_role: immutable_course_content_for_round_1
status: READY_NOT_RUN
round_1: READY_NOT_RUN
round_2: NOT_AUTHORIZED_BEFORE_ROUND_1_REVIEW
round_3: NOT_AUTHORIZED_BEFORE_PATCH
results_exist: false
```

Round 1 必须以冻结 commit 的五课授课稿、五张主工具和 Deck 蓝图为唯一课程输入。

## 三轮结构

### Round 1｜Blind Run

- P01 方法很多型专家
- P02 成熟经营型企业家
- P03 专家 IP 型创业者

三位 Persona 均连续走完 L01→L05，共 15 个纵向 Session。

规则：本轮结束前不修改课程正文。

### Round 2｜Adversarial Run

- P04 AI 工具狂热者：重点攻击 L04；
- P05 高成就效率主义者：重点攻击 L05；
- Red Team 横向攻击 L01—L05 的关键误解。

只有 Round 1 汇总完成后才可授权。

### Round 3｜Regression Run

完成 P0/P1 Patch 后，必须创建一个全新、从未见过课程的 Persona F，从 L01 完整走到 L05。

原 Persona 不得用于证明修复有效。

## 五角色分权

- **Teacher**：严格按冻结课程讲，不临时扩写救场。
- **Blind Learner**：只使用当前已讲内容，必须暴露困惑与误解。
- **Observer**：只记录，不教学、不补答案。
- **Examiner**：闭卷检测“说得出、分得清、对得上、用得起”。
- **Red Team**：主动诱导危险误解，测试学员能否拒绝错误解释。

## 单课评分七维

每项 1—5：

- Hit｜被击中
- Comprehension｜听懂
- Discrimination｜分得清
- Self-Mapping｜对号入座
- Toolability｜用得起
- Load｜认知负荷控制
- Pull｜对下一课的自然牵引

## 单课 Green Gate

```yaml
comprehension: ">=4/5"
discrimination: ">=4/5"
self_mapping: ">=4/5"
tool_quality: "Level 3"
narrative_pull: ">=4/5"
critical_misconceptions: 0
load_red_zones: 0
```

## 五课整体 Green Gate

```yaml
five_lesson_spine_recall: PASS
A_B_C_canon_confusion: 0
yuanli_life_as_part4_confusion: 0
B4_fifth_barrier_confusion: 0
C5_confusion: 0
five_tools_reconstructable: PASS
lesson_handoffs: 4/4_PASS
new_persona_regression: PASS
```

## 目录

```text
README.md
protocol.md

personas/
  P01-method-rich-expert.yaml
  P02-pragmatic-founder.yaml
  P03-expert-ip.yaml
  P04-ai-tool-maximalist.yaml
  P05-achievement-maximalist.yaml

sessions/
  L01/SESSION-TEMPLATE.md
  L02/SESSION-TEMPLATE.md
  L03/SESSION-TEMPLATE.md
  L04/SESSION-TEMPLATE.md
  L05/SESSION-TEMPLATE.md

ledgers/
  misconception-ledger.md
  cognitive-load-ledger.md
  tool-completion-ledger.md
  narrative-handoff-ledger.md

cross-course/
  five-course-reconstruction.md
  context-isolated-recall.md

patch-candidates.md
DESKTOP-TRIAL-RECEIPT.yaml
```

## 当前闸门

当前只完成 Trial Contract 与执行骨架。

**没有任何模拟结果。**

下一次授权动作应是：

> Run Round 1 / P01-P03 / 15 Sessions against frozen snapshot.
