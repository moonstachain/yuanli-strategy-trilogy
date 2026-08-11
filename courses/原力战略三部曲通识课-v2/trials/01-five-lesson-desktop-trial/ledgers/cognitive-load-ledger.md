# Cognitive Load Ledger｜认知负荷总账

> 当前状态：ROUND_2_POPULATED / PATCH_NOT_APPLIED

## 采样规则

```text
1—3 = Green
4—5 = Yellow
6+  = Red
```

| Round | Persona | Lesson | Time window | Active novel concepts | Dropped / threatened concept | Load color | Evidence | Patch ID |
|---|---|---|---|---:|---|---|---|---|
| 1 | P01 | L02 | 31—77 | 6 | `见名繁守`与“一势两账三链四权”竞争主记忆 | Red | P01-L02 | PATCH-P1-03 |
| 1 | P01 | L03 | 78—87 | 7 | 反证/取舍/判断规则/90天实验无法同时高质量完成 | Red | P01-L03 | PATCH-P1-01 |
| 1 | P01 | L04 | 32—76 | 6—7 | C1—C4主线被Cited/Unknown、三类能力、五级现实链挤压 | Red | P01-L04 | PATCH-P1-04 |
| 1 | P01 | L04 | 84—88 | 8 | 工具字段挤压Outcome/Reuse | Red | P01-L04 | PATCH-P1-02 |
| 1 | P02 | L03 | 78—87 | 7 | 为赶工具而把母体重新压成“核心竞争力” | Red | P02-L03 | PATCH-P0-01 / PATCH-P1-01 |
| 1 | P02 | L04 | 84—88 | 7 | Outcome/Reuse来不及完成 | Red | P02-L04 | PATCH-P1-02 |
| 1 | P03 | L03 | 78—87 | 7 | 反证与90天验证最先被草率处理 | Red | P03-L03 | PATCH-P1-01 |
| 1 | P03 | L04 | 84—88 | 7 | Reuse字段未完成 | Red | P03-L04 | PATCH-P1-02 |
| 2 | P04 | L04 | 30—45 | 6 | C2母问题被事实/证据/判断/Outcome/Learning与Cited/Inferred/Unknown挤压 | Red | P04-L04 | PATCH-P1-04 |
| 2 | P04 | L04 | 60—75 | 6 | C4母问题被五级现实链+Human Gate+Reuse挤压 | Red | P04-L04 | PATCH-P1-04 |
| 2 | P05 | L05 | 0—90 | 3—5 | 无持续掉线；主要摩擦是把价值重新KPI化 | Green/Yellow | P05-L05 | PATCH-P2-03 |

## Round 1 Lesson-Level Signal

| Lesson | Hit avg | Comprehension avg | Discrimination avg | Self-Mapping avg | Toolability avg | Load avg | Pull avg | Load verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| L01 | 5.00 | 4.00 | 3.33 | 5.00 | 4.00 | 4.00 | 5.00 | Green/Yellow |
| L02 | 5.00 | 4.33 | 3.67 | 5.00 | 4.33 | 3.67 | 4.00 | Persona-sensitive Red in P01 |
| L03 | 4.33 | 3.67 | 3.33 | 4.33 | **1.67** | 3.00 | 4.67 | **Systemic tool-stage Red** |
| L04 | 5.00 | 4.00 | 4.00 | 5.00 | **2.33** | **2.67** | 5.00 | **Systemic middle/tool Red** |
| L05 | 4.33 | 4.33 | 4.00 | 4.33 | 4.00 | 4.00 | 4.00 | Green/Yellow |

## Round 2 Findings

1. **P04再次复现L04两个Red窗口。** 说明L04负荷不是“方法很多型学员”的个人偏好，而是对高AI熟练者也成立。
2. P04最终仍能守住C1—C4边界，所以修法应是**降二级框架记忆要求**，不是删掉Human Gate/Outcome/Reuse。
3. P05没有系统性Red，L05的主要问题是目标最大化偏见与轻度工具超时，不是概念密度崩塌。
4. L03系统性Red仍由Round1三位纵向Persona充分成立，Round2没有新课程Patch前不再重复跑普通理解。

```yaml
round_2_load_result: CONFIRMS_EXISTING_BLOCKERS
systemic_red_lessons: [L03, L04]
new_systemic_red_lesson: none
PATCH_P1_04_confidence: increased
```
