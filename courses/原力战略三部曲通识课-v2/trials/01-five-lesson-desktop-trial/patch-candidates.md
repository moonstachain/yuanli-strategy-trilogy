# Patch Candidates｜课程修订候选队列

> 当前状态：ROUND_2_REVIEWED / NOT_APPLIED

## 纪律

- Round 1 / Round 2 均使用冻结课程快照；
- 下面全部是候选，不是已经执行的修订；
- P0/P1 必须有 Session / Red Team 证据和 Regression Target；
- 优先删、移、重排、做强判别，不用新增更多概念解决概念过载；
- Round 3 前必须经 Human Gate 裁决并应用后重新冻结。

## Patch Queue

| Patch ID | Severity | Lesson | Misconception / Block | Evidence refs | Root cause | Minimal patch | Expected side effect | Regression target | Decision |
|---|---|---|---|---|---|---|---|---|---|
| **PATCH-P0-01** | **P0** | L03 | 母体被稳定压缩成“底层核心竞争力/核心能力” | P02-L03 + P02 isolated recall + Round2 Red Team | `definition_ambiguity + example_mismatch` | 在“五层追问”后加入**同一生成机制→三种不同能力/职业载体**的对照案例；增加闭卷判别：“如果一句话仍可直接写进能力清单，它为什么还不是母体？”；母体卡第一步先写“生成动作”，再写能力表型 | 约增加3分钟，必须从重复定义/示例中回收，不延长总课时 | Persona F 必须区分 `generator != capability`；Red Team不得再把母体压成核心竞争力 | **PROPOSED_REQUIRED / ROUND2_CONFIRMED** |
| **PATCH-P0-02** | **P0** | L02 | 品类被稳定压缩成“占领定位词/超级标签” | P03-L02 + P03 isolated recall + Round2 Red Team | `definition_ambiguity + prior_IP_schema` | 将工具“暂定名字/品类”拆成：`旧分类/旧比较对象 → 新分类/新比较对象`；**名字改成可选最后一步**；加入“漂亮名字但用户分类没变 / 名字普通但比较维度已变”的强对照 | 工具字段重排，不增加总概念数 | Persona F 必须说明为什么好名字≠新品类；Red Team“名=起名”不得击穿 | **PROPOSED_REQUIRED / ROUND2_CONFIRMED** |
| **PATCH-P1-01** | **P1** | L03 | 九格母体假设卡最后9分钟，3/3 Persona无法达到L3 | P01/P02/P03-L03 | `sequence_error + concept_overload` | 不删反证与验证；改为**随课分段填写**：A1填1—6，A2填7，A3填8，A4填9；最后只做整合/闭卷 | 课堂互动更频繁，最后集中书写显著减少 | Persona F：L03等价工作量≤15min且L3；反证不得为空 | **PROPOSED_REQUIRED** |
| **PATCH-P1-02** | **P1** | L04 | OS一页架构集中在最后4分钟，Round1 3/3失败；P04仍需约14分钟 | P01/P02/P03-L04 + P04-L04 | `sequence_error + concept_overload` | C1/C2/C3/C4讲完即填写对应格；84—88分钟只完成回写/复用与整合；保持Outcome/Reuse硬门槛 | 由“先听后填”变成“边学边建” | Persona F：L04≤15min且必须含Outcome+Reuse | **PROPOSED_REQUIRED / ROUND2_CONFIRMED** |
| **PATCH-P1-03** | **P1** | L02 | P01被“一势两账三链四权”截流，L2→L3 Handoff=3 | P01-L02 + Narrative Ledger | `concept_overload + handoff_failure` | 通识课前台只保留“见名繁守+四财富”；“一势两账三链四权”降为讲师备注/附录或每段轻提，不再集中形成第二套口诀 | 专业感略降，但主叙事更强 | Persona F：L02结束自然问题指向“为什么是我”，不先索要三链/四权深挖 | **PROPOSED_REQUIRED** |
| **PATCH-P1-04** | **P1** | L04 | C2/C3/C4二级框架与C1—C4竞争工作记忆；P04复现两个Red窗口 | P01-L04 + Cognitive Load Ledger + P04-L04 | `concept_overload` | C1—C4母图始终常驻；Cited/Inferred/Unknown、三类能力、五级现实链改成案例标签，不要求闭卷记忆；验收只考“原则/证据/押注/执行/回写” | 减术语密度，不改正典与Human Gate | Persona F：L04无连续Red窗口；P04型回归仍能拒绝OS=工具栈 | **PROPOSED_REQUIRED / ROUND2_CONFIRMED** |
| PATCH-P2-01 | P2 | L05 | 工具轻度超时：P01 16min，P05 15min，高于14min目标 | P01-L05 + P05-L05 | `tool_prompt_density` | 2036字段改为课后延伸或一句极短句；五个必填裁决字段不删 | 少量减少情绪收束书写 | Persona F：L05≤14min且保留真实tradeoff | **OPTIONAL / ROUND2_CONFIRMED** |
| PATCH-P2-02 | P2 | L05 | “生”可能被写成核心能力或品牌使命 | P02/P03-L05 | `cross_lesson_reference_ambiguity` | 增加一句：“第三课问生成源是什么；第五课不重新定义母体，只问希望它长期生成什么。” | 无明显副作用 | Persona F：`生`不等于能力/使命标签 | OPTIONAL |
| PATCH-P2-03 | P2 | L05 | 高成就Persona会把“守生事人留”重新做成五维KPI/Scorecard | P05-L05 + Round2 Red Team | `goal_maximization_bias` | 在“价值=裁决函数”后加一个判别：**有些东西是要最大化的目标，有些东西是成功不可突破的约束；‘守’首先属于后者。** 不新增框架名 | 增加约1分钟，需要从例子中回收 | Persona F/P05型回归能说明“价值约束≠KPI权重” | OPTIONAL |

## Watch Items｜不进入当前强制Patch

### W-01｜L01 “只有你才能发现”前台绝对化

Round 2 Red Team 能被现有“更可能先看见 + 可验证”边界纠正，因此暂不升级Patch。

Round 3 观察：

> Persona F 是否自然理解为“你更可能持续看见/生成的差异”，而不是排他天命。

若再次出现稳定排他解释，再升级为P1/P2。

---

## Priority Order After Round 2

```text
1. PATCH-P0-01 母体 vs 核心竞争力
2. PATCH-P0-02 品类 vs 定位词
3. PATCH-P1-01 L03工具分段
4. PATCH-P1-02 L04工具分段
5. PATCH-P1-03 L02第二套口诀降级
6. PATCH-P1-04 L04二级框架降负荷
7. P2节奏/判别优化
```

## Round 2 Patch Gate

```yaml
P0_count: 2
P1_count: 4
P2_count: 3
watch_items: 1
patches_applied: 0
round_2_new_P0: 0
round_2_confirmed_existing_P0: 2
round_2_confirmed_existing_P1: 2
course_snapshot_mutated_during_round_2: false
patch_required_before_regression: true
human_gate_required_before_patch: true
```

## 下一允许的修订阶段

Round 2完成后，只有在 Human Gate 明确批准后，才允许：

```text
Apply approved P0/P1 (and selected P2)
→ create patched snapshot
→ create brand-new Persona F
→ run Round 3 Regression
```

没有新Persona、没有重新冻结快照，不得以原Persona证明修复有效。
