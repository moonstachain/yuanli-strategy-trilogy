# Misconception Ledger｜危险误解总账

> 当前状态：ROUND_1_POPULATED

## 记录规则

每条误解必须引用具体 Session，不写“感觉学员可能误解”。

| ID | Round | Persona | Lesson | Raw learner statement / observed compression | Severity | Persistence | Expected concept | Root cause hypothesis | Patch ID |
|---|---:|---|---|---|---|---|---|---|---|
| M-001 | 1 | P02 | L03 | “母体就是最稳定、最底层的核心竞争力/核心能力。” | **P0** | Session exit + isolated recall | 母体是持续生成多种能力/判断/作品的生成机制，不是能力本身 | `definition_ambiguity + example_mismatch + tool_time_pressure` | PATCH-P0-01 |
| M-002 | 1 | P03 | L02 | “名最终还是找到一个用户能记住、最好由我占领的定位词。” | **P0** | Session exit + isolated recall | 品类是价值进入市场的认知接口，包含分类、比较维度、问题解释与估值，不等于命名词 | `definition_ambiguity + existing_schema_assimilation` | PATCH-P0-02 |
| M-003 | 1 | P03 | L01 | “秘密很像我的独特内容定位/选题。” | P1 / resolved later | L01 exit partial；L02秘密三道门后基本纠正 | 秘密是变化×贵问题×可验证新答案 | `prior_IP_schema` | — |
| M-004 | 1 | P03 | L03 | “母体可能是智者/探索者/结构化天赋。” | P1 / resolved in lesson | L03中段后纠正，isolated recall未复发 | Mother Hypothesis + evidence + counter-evidence | `identity_label_bias` | — |
| M-005 | 1 | P03 | L04 | “OS就是内容库+Agent+自动分发。” | P1 / resolved in lesson | L04结束后纠正，isolated recall未复发 | C1—C4控制循环 + Outcome/Learning/Reuse | `tool_stack_bias` | — |
| M-006 | 1 | P01 | L01 | “那我得找一个AI不会的稀缺技能。” | P1 / resolved in lesson | 未持续 | 经营独特生成而非技能避难所 | `starting_belief` | — |

## Critical Misconception Result

```yaml
persistent_critical_misconceptions: 2
items:
  - M-001 mother_equals_core_competency
  - M-002 category_equals_positioning_word
round_1_critical_gate: FAIL
```

## 正典硬边界检查

以下 Round 1 均为 0：

```yaml
B_to_A_to_C_as_new_canon: 0
B4_fifth_barrier: 0
mother_as_fixed_destiny: 0
C3_as_mindmap_only: 0
C5_exists: 0
yuanli_life_as_part4: 0
desktop_evidence_as_real_learner_evidence: 0
```

说明：本轮发现的两个 P0 属于**教学概念压缩错误**，不是 Soul 正典本身被课程改写。
