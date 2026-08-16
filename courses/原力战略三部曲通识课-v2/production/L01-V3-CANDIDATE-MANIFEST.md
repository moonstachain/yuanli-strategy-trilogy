# Production Manifest｜L01 V3 Candidate

```yaml
candidate_id: YL-TRILOGY-GENERAL-v2-L01-V3-CANDIDATE
course_id: YL-TRILOGY-GENERAL-v2
layer: production_candidate
status: REVISE_BEFORE_LIVE
created_at: 2026-08-16
last_trial_at: 2026-08-16
canon_effect: none
current_L01_replaced: false
desktop_trial: EVIDENCE_AVAILABLE_REVISE
context_isolated_recall_proxy: COMPLETE_WITH_ONE_CRITICAL_DRIFT
real_24h_recall: NOT_RUN
live_trial: NOT_READY_PATCH_REQUIRED
promotion: NOT_AUTHORIZED
patch_gate: AWAITING_HUMAN_RULING
```

## 1. 生产目的

本文件只登记一个 Overlay Candidate，不改变现役 V2 五课生产状态。

现役 L01 继续保持当前合法基线；V3 只有在补丁回归、真人 Trial 与 Human Promotion Gate 通过后，才允许替换。

## 2. Candidate 资产清单

- Evolution：`../evolution/09-L01-AI时代新财富算法-v3-Evolution-Note.md`
- Evidence：`../evidence/L01-文明理论三角-Evidence-Packet-v1.md`
- Lesson：`../lessons/secret-life/L01-秘密诞生-原力战略-v3-candidate.md`
- Director：`../director/secret-life/L01-90MIN-DIRECTOR-v3-candidate.md`
- Deck：`../deck/secret-life/01-原力战略-AI时代新财富算法-PPT蓝图-v3.md`
- Artifact：`../exercises/secret-life/L01-AI时代我的价值清算表-v2.md`
- Trial Protocol：`../trials/08-l01-new-wealth-v3/README.md`
- Round 1：`../trials/08-l01-new-wealth-v3/ROUND-1-PERSONA-SESSIONS.md`
- Red Team：`../trials/08-l01-new-wealth-v3/ROUND-2-RED-TEAM.md`
- Recall Proxy：`../trials/08-l01-new-wealth-v3/CONTEXT-ISOLATED-RECALL-PROXY.md`
- A/B：`../trials/08-l01-new-wealth-v3/AB-COMPARISON-V2-V3.md`
- Patch Queue：`../trials/08-l01-new-wealth-v3/PATCH-CANDIDATES.md`
- Result：`../trials/08-l01-new-wealth-v3/RESULT-v1.md`

## 3. 上游理论

Soul Candidate Extension：

`moonstachain/yuanli-strategy-soul/curriculum/extensions/AI时代新财富算法-v1/`

法权：`teaching_framework / canon_effect:none`。

## 4. 保留现役资产

以下不删除、不覆盖：

- `../director/L01-原力战略-导演脚本.md`
- `../lessons/01-原力战略-AI时代的新财富.md`
- `../lessons/secret-life/L01-秘密诞生-原力战略.md`
- 现役 Secret-Life Director / Deck / Desktop Trial 收据
- 1455 古腾堡与 1997 Deep Blue Anchor

## 5. Candidate 状态

```text
Theory Extension       READY
Evidence Packet        READY_WITH_BOUNDARIES
Lesson Candidate       FROZEN_FOR_TRIAL_08
90min Director         FROZEN_FOR_TRIAL_08
Deck Blueprint         READY
Artifact               BLOCKED_BY_TIME_BUDGET
Desktop Evidence       AVAILABLE
Red Team                COMPLETE
V2/V3 A-B               COMPLETE_DIRECTIONAL
Recall Proxy            PASS_WITH_ONE_CRITICAL_DRIFT
Real 24h Recall         NOT_RUN
Patch Candidates        RECORDED_NOT_APPLIED
Human Patch Gate        AWAITING_RULING
Live Trial              NOT_READY_PATCH_REQUIRED
Promotion               NOT_AUTHORIZED
```

## 6. Desktop Gate Failure Reasons

1. `Critical Misconception recurrence > 0`：P02 将秘密重新压缩为商业机会；
2. Artifact 当前无独立课内时间槽，P01-P05 估时 15—19min，超过既有 L01 `≤13min` Desktop Budget；
3. L02 Handoff 被 L03/L05 竞争；
4. P02/P04 出现高 Cognitive Load 峰值。

## 7. 当前裁决

> **V3 的理论发动机保留，但当前版本不得进入真人试讲。**

状态：

```yaml
decision: REVISE_BEFORE_LIVE
```

## 8. 下一合法动作

> **Human Patch Gate → 应用最小补丁 → 冻结 V3.1 snapshot → 新一轮 regression → 再判断 LIVE_TRIAL_READY。**

推荐 Patch Set 已在 `PATCH-CANDIDATES.md` 冻结，尚未应用。

不得：

- 把 Context-Isolated Recall 冒充真实 24h；
- 直接标记 `validated_live`；
- 覆盖现役 V2；
- Promotion；
- Canon upgrade。
