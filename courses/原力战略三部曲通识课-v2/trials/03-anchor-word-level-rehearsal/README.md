# 10 Anchor Word-level Rehearsal

> 状态：`READY_NOT_RUN`

```yaml
trial_id: YL-TRILOGY-GENERAL-v2-ANCHOR-REHEARSAL-001
scope: 10_word_level_anchor_scripts
status: READY_NOT_RUN
requires_human_speaker: true
requires_real_timer: true
synthetic_readthrough_insufficient_for_pass: true
recording_authorized: false
live_trial_authorized: false
```

## 一、目的

逐字稿已经完成，不代表可以直接录。

本轮只验证：

1. 真实口播时长是否落在 8—15 分钟；
2. `[PAUSE]` 是否自然，不被讲师下意识填满；
3. 史料数字是否在口播中清楚、不造成记忆过载；
4. `[ARC]` 是否真的成为唯一记忆峰值；
5. `[DEEP_DIVE]` 是否解释机制而不是变成百科；
6. `[CONCEPT_REVEAL]` 是否过早或过晚；
7. `[PERSONAL_VERDICT]` 是否能在 45—90 秒内完成；
8. 两个 Anchor 是否挤压五课唯一工具与课尾悬念。

---

## 二、十稿逐项记录

每个 Anchor 完成一次真人口播后填写：

```yaml
anchor_id:
rehearsal_date:
speaker:
actual_runtime:
scene_entry_under_60s: unknown
anomaly_clear: unknown
dilemma_feels_real: unknown
fact_density: unknown
pause_respected: unknown
arc_single_peak: unknown
deep_dive_overload: unknown
concept_reveal_timing: unknown
personal_verdict_time:
script_edits_required: []
status: NOT_RUN
```

---

## 三、逐稿 PASS 条件

单个 Anchor 至少满足：

- `actual_runtime` 在 8—15 分钟；
- 60 秒内进入具体现场；
- 异常不需要讲师解释两遍；
- 两难后真实留白 ≥ 5 秒；
- 史料数字不超过学员短时记忆承载；
- 主弧光只有一个；
- 纵深能用一句话复原共同机制；
- 概念命名发生在故事主要事实之后；
- PERSONAL_VERDICT 不是感悟题；
- 不新增未经证据包支持的史实。

---

## 四、课程级时间预算

```yaml
L01_anchor_budget: 20min
L02_anchor_budget: 22min
L03_anchor_budget: 24min
L04_anchor_budget: 20min
L05_anchor_budget: 20min
```

如果真人口播超预算，裁剪优先级：

```text
先删：重复解释 / 第三个类比 / 第二层背景史

后删：非必要数字

不能删：异常 / 两难 / 硬证据 / 主弧光 / 概念命名 / PERSONAL_VERDICT
```

---

## 五、全局 PASS 条件

10/10 单稿通过后仍不能直接宣称 Live Trial 通过。

本轮只允许状态升级为：

```text
SCRIPT_READY
→ REHEARSAL_PASS
→ RECORDING_READY
```

真人学员效果仍必须进入上一层：

> `../02-anchor-cut-live-trial/`

验证 24h 记忆、迁移、FACT/INTERPRET 分离与工具质量。

---

## 六、当前状态

```yaml
A01: NOT_RUN
A02: NOT_RUN
A03: NOT_RUN
A04: NOT_RUN
A05: NOT_RUN
A06: NOT_RUN
A07: NOT_RUN
A08: NOT_RUN
A09: NOT_RUN
A10: NOT_RUN
overall: READY_NOT_RUN
```
