# Cognitive Load Ledger｜认知负荷总账

> 当前状态：ROUND_1_POPULATED

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
| 1 | P01 | L04 | 32—76 | 6—7 | C1—C4主线被Cited/Unknown、三类能力、五级现实链挤压 | Red | P01-L04 | PATCH-P1-02 |
| 1 | P01 | L04 | 84—88 | 8 | 工具字段挤压Outcome/Reuse | Red | P01-L04 | PATCH-P1-02 |
| 1 | P02 | L03 | 78—87 | 7 | 为赶工具而把母体重新压成“核心竞争力” | Red | P02-L03 | PATCH-P0-01 / PATCH-P1-01 |
| 1 | P02 | L04 | 84—88 | 7 | Outcome/Reuse来不及完成 | Red | P02-L04 | PATCH-P1-02 |
| 1 | P03 | L03 | 78—87 | 7 | 反证与90天验证最先被草率处理 | Red | P03-L03 | PATCH-P1-01 |
| 1 | P03 | L04 | 84—88 | 7 | Reuse字段未完成 | Red | P03-L04 | PATCH-P1-02 |

## Lesson-Level Signal

| Lesson | Hit avg | Comprehension avg | Discrimination avg | Self-Mapping avg | Toolability avg | Load avg | Pull avg | Load verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| L01 | 5.00 | 4.00 | 3.33 | 5.00 | 4.00 | 4.00 | 5.00 | Green/Yellow |
| L02 | 5.00 | 4.33 | 3.67 | 5.00 | 4.33 | 3.67 | 4.00 | Persona-sensitive Red in P01 |
| L03 | 4.33 | 3.67 | 3.33 | 4.33 | **1.67** | 3.00 | 4.67 | **Systemic tool-stage Red** |
| L04 | 5.00 | 4.00 | 4.00 | 5.00 | **2.33** | **2.67** | 5.00 | **Systemic middle/tool Red** |
| L05 | 4.33 | 4.33 | 4.00 | 4.33 | 4.00 | 4.00 | 4.00 | Green/Yellow |

## Round 1 Load Findings

1. **L03工具阶段 3/3 Persona 进入Red。**
2. **L04工具阶段 3/3 Persona 进入Red。**
3. L04还存在中段概念堆叠问题：四器官主线之外同时引入知识状态、能力类型、现实链与Human Gate/Reuse。
4. L02负荷不是普遍失败：P02/P03可承受，P01因方法收藏倾向出现第二套主框架竞争。
5. L01、L05没有系统性Red。

```yaml
round_1_load_gate: FAIL
systemic_red_lessons: [L03, L04]
```
