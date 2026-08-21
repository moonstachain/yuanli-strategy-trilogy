# Production Manifest｜L01 V3.1 Candidate

```yaml
candidate_id: YL-TRILOGY-GENERAL-v2-L01-V3.1-CANDIDATE
course_id: YL-TRILOGY-GENERAL-v2
layer: production_candidate
status: LIVE_TRIAL_READY
created_at: 2026-08-16
last_trial_at: 2026-08-16
canon_effect: none
current_L01_replaced: false
human_patch_gate: APPROVED
frozen_snapshot_branch: snapshot/l01-v3.1-20260816
frozen_snapshot_sha: eda55d3d653c03ba2c3b78822745e80f1b9b10f3
desktop_trial: PASS_SIMULATED
context_isolated_recall_proxy: PASS_6_OF_6
real_24h_recall: NOT_RUN
live_trial: READY_NOT_RUN
promotion: NOT_AUTHORIZED
```

## 1. 生产目的

本文件登记 L01 V3.1 Overlay Candidate 的当前合法状态。

现役 V2 L01 仍保持合法基线；V3.1 已通过模拟桌面回归，因此**获得进入真人试讲的制作资格**，但尚未获得替换 V2 的 Promotion 法权。

---

# 2. V3.1 主资产

- Lesson：`../lessons/secret-life/L01-秘密诞生-原力战略-v3.1-candidate.md`
- Director：`../director/secret-life/L01-90MIN-DIRECTOR-v3.1-candidate.md`
- Deck：`../deck/secret-life/01-原力战略-AI时代新财富算法-PPT蓝图-v3.1.md`
- Artifact：`../exercises/secret-life/L01-AI时代我的价值清算表-v3.1.md`
- Evidence：`../evidence/L01-文明理论三角-Evidence-Packet-v1.md`
- Evolution：`../evolution/09-L01-AI时代新财富算法-v3-Evolution-Note.md`

## 3. Trial 08 Evidence

### V3 初轮

- `../trials/08-l01-new-wealth-v3/RESULT-v1.md`
- `ROUND-1-PERSONA-SESSIONS.md`
- `ROUND-2-RED-TEAM.md`
- `CONTEXT-ISOLATED-RECALL-PROXY.md`
- `AB-COMPARISON-V2-V3.md`
- `PATCH-CANDIDATES.md`

### V3.1 回归

- `../trials/08-l01-new-wealth-v3/HUMAN-GATE.md`
- `V3.1-SNAPSHOT.md`
- `V3.1-REGRESSION-SESSIONS.md`
- `V3.1-CONTEXT-ISOLATED-RECALL-PROXY.md`
- `RESULT-v2-V3.1.md`

---

# 4. Human-approved Patch Set

```text
P0-01 秘密 ≠ 商业机会
P1-01 Live Core Artifact 10—12min
P1-02 三本书脚注化 + 稀缺阶梯压缩
P1-03 关闭 L03/L05 竞争悬念，只留 L02
P1-04 Value Candidate ≠ 唯一使命
```

---

# 5. Regression Result

```yaml
critical_secret_misconception_recurrence: 0_of_6
opportunity_secret_boundary: PASS_6_OF_6
value_candidate_missionization: 0_of_6
artifact_L3: 6_of_6
artifact_estimated_time_range: 9-12min
P02_cognitive_peak: YELLOW_NOT_RED
P04_cognitive_peak: MEDIUM_NOT_RED
L02_first_handoff: 6_of_6
context_isolated_recall_proxy: PASS_6_OF_6
canon_boundary_breach: 0
teacher_rescue_required: 0
```

Desktop Verdict：

> **PASS_FOR_LIVE_TRIAL_READINESS**

---

# 6. 当前合法状态

```text
Theory Extension       READY
Evidence Packet        READY_WITH_BOUNDARIES
V3.1 Lesson             FROZEN
V3.1 Director           FROZEN
V3.1 Deck               FROZEN
V3.1 Artifact           FROZEN
Desktop Regression      PASS_SIMULATED
Recall Proxy            PASS_6_OF_6
Real 24h Recall         NOT_RUN
Live Trial              READY_NOT_RUN
Promotion               NOT_AUTHORIZED
```

---

# 7. 保留现役资产

以下不删除、不覆盖：

- `../director/L01-原力战略-导演脚本.md`
- `../lessons/01-原力战略-AI时代的新财富.md`
- `../lessons/secret-life/L01-秘密诞生-原力战略.md`
- 现役 Secret-Life Director / Deck / Desktop Trial 收据
- 1455 古腾堡与 1997 Deep Blue Anchor

---

# 8. 下一合法动作

> **执行 L01 V3.1 真人试讲，采集真实课堂证据。**

真人试讲之后必须继续：

```text
Live Trial
→ Live Evidence
→ 真实24h Recall
→ V2 / V3.1 Human A/B Review
→ Promotion Decision
```

不得：

- 把 simulated completion time 当真实课堂时间；
- 把 Context-Isolated Recall Proxy 当真实 24h Recall；
- 自动替换 V2；
- 标记 `validated_live`；
- Promotion；
- Canon upgrade。
