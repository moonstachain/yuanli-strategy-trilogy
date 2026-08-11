# Patch Candidates｜课程修订候选队列

> 当前状态：ROUND_1_REVIEWED / NOT_APPLIED

## 纪律

- Round 1 冻结课程没有被修改；
- 下面全部是候选，不是已经执行的修订；
- P0/P1必须有Session证据和Regression Target；
- 优先删、移、重排，不用新增更多概念解决概念过载。

## Patch Queue

| Patch ID | Severity | Lesson | Misconception / Block | Evidence refs | Root cause | Minimal patch | Expected side effect | Regression target | Decision |
|---|---|---|---|---|---|---|---|---|---|
| **PATCH-P0-01** | **P0** | L03 | 母体被P02稳定压缩成“底层核心竞争力/核心能力” | P02-L03 + P02 isolated recall | `definition_ambiguity + example_mismatch` | 在“五层追问”后插入一组**同一生成机制→三种不同能力/职业载体**的具体商业案例；增加闭卷判别题：“如果一句话仍可直接写进能力清单，它为什么还不是母体？”；不新增新术语 | 约增加3—4分钟，需从后文示例回收时间 | Round2 P05/P04边界攻击；Round3 Persona F 必须区分 `generator != capability` | PROPOSED_REQUIRED |
| **PATCH-P0-02** | **P0** | L02 | 品类被P03稳定压缩成“占领定位词/超级标签” | P03-L02 + P03 isolated recall | `definition_ambiguity + prior_IP_schema` | 将工具“暂定名字/品类”拆成：`旧分类/旧比较对象 → 新分类/新比较对象`，**名字改为可选最后一步**；课堂增加“一样的名字但比较维度改变 / 漂亮名字但用户分类没变”的对照 | 工具字段略变，但不增加总概念数 | Round2 Red Team故意诱导“品类=命名”；Round3 Persona F 必须能说明为什么好名字≠新品类 | PROPOSED_REQUIRED |
| **PATCH-P1-01** | **P1** | L03 | 九格母体假设卡在最后9分钟，3/3 Persona无法达到L3 | P01/P02/P03-L03 | `sequence_error + concept_overload` | 不删反证与验证字段；改为**随课分段填写**：A1填1—6，A2填7，A3填8，A4填9；最后9分钟只做整合/闭卷 | 课堂互动更频繁，减少最后集中书写 | Round3 Persona F：L03工具≤15min等价工作量且L3 | PROPOSED_REQUIRED |
| **PATCH-P1-02** | **P1** | L04 | 一页OS架构集中在最后4分钟，3/3 Persona无法完成Outcome+Reuse | P01/P02/P03-L04 | `sequence_error + concept_overload` | C1/C2/C3/C4讲完即填写对应格；84—88分钟只完成回写/复用与整合；保持Outcome/Reuse硬门槛 | 课程由“先听后填”变成“边学边建” | Round3 Persona F：L04工具≤15min且必须含Outcome+Reuse | PROPOSED_REQUIRED |
| **PATCH-P1-03** | **P1** | L02 | P01被“一势两账三链四权”截流，L2→L3 Handoff=3 | P01-L02 + Narrative Ledger | `concept_overload + handoff_failure` | 通识课前台只保留“见名繁守+四财富”；“一势两账三链四权”降为讲师备注/附录或每段只轻提，不再集中形成第二套口诀 | 可能降低专业感，但提高主线记忆和课间牵引 | Round3 Persona F：L02结束自然问题必须指向“为什么是我”，且不先索要三链/四权深挖 | PROPOSED_REQUIRED |
| PATCH-P1-04 | P1 | L04 | 中段二级框架叠加：知识状态、三类能力、五级现实链与C1—C4竞争工作记忆 | P01-L04 + Cognitive Load Ledger | `concept_overload` | 保留C1—C4为屏幕常驻母图；二级框架改为例子中的小标签，不要求闭卷记忆；课堂验收只考“原则/证据/押注/执行/回写” | 减少术语密度，不改变正典内容 | Round2 P04工具狂热攻击；Round3 L04无连续Red窗口 | PROPOSED |
| PATCH-P2-01 | P2 | L05 | P01一页纸估算16分钟，高于14分钟目标 | P01-L05 | `tool_prompt_density` | 把2036字段设为课后延伸或允许一句极短句，不影响五个必填裁决字段 | 轻微减少情绪收束时间 | Round3 L05≤14min | OPTIONAL |
| PATCH-P2-02 | P2 | L05 | “生”可能被P02/P03写成核心能力或品牌使命 | P02/P03-L05 | `cross_lesson_reference_ambiguity` | 增加一句边界：“第三课问生成源是什么；第五课不再重新定义母体，只问希望它长期生成什么。” | 无明显副作用 | Round3 Persona F `生`不等于能力/使命标签 | OPTIONAL |

## Priority Order

```text
P0概念边界
→ P1工具分段
→ P1叙事/负荷
→ P2节奏措辞
```

## Round 1 Patch Gate

```yaml
P0_count: 2
P1_count: 4
P2_count: 2
patches_applied: 0
course_snapshot_mutated_during_round_1: false
patch_required_before_regression: true
```
