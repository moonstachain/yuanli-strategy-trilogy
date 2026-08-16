# Trial 08｜L01「AI时代的新财富算法」V3 Candidate

```yaml
trial_id: YL-L01-V3-TRIAL-08
candidate_id: YL-TRILOGY-GENERAL-v2-L01-V3-CANDIDATE
status: REVISE_BEFORE_LIVE
trial_type:
  - desktop
  - live
  - 24h_recall
promotion_authority: human
canon_effect: none
desktop_trial: EVIDENCE_AVAILABLE_REVISE
context_isolated_recall_proxy: COMPLETE
real_24h_recall: NOT_RUN
live_trial: NOT_READY_PATCH_REQUIRED
promotion: NOT_AUTHORIZED
```

## 0. 本轮执行结果｜2026-08-16

已完成：

- `ROUND-1-PERSONA-SESSIONS.md`：P01/P02/P03；
- `ROUND-2-RED-TEAM.md`：P04/P05；
- `CONTEXT-ISOLATED-RECALL-PROXY.md`：P01-P06；
- `AB-COMPARISON-V2-V3.md`：V2 vs V3 方向性 Desktop A/B；
- `PATCH-CANDIDATES.md`：1 个 P0、4 个 P1/P1 blocker、1 个 P2；
- `RESULT-v1.md`：Live Gate 总裁决。

总裁决：

> **V3 的理论发动机已经赢，但当前课程工程仍未达到真人试讲门槛。**

当前必须修复：

1. P02 的“秘密 = 商业机会”关键漂移；
2. Artifact 无独立课内时间槽、预计 15—19min，超过既有 L01 ≤13min Desktop Budget；
3. L02 Handoff 被 L03/L05 竞争；
4. 三本书 + 稀缺阶梯造成部分 Persona 高负荷。

下一合法动作：

> **Human Patch Gate → V3.1 minimal patch → regression → 再裁决是否 LIVE_TRIAL_READY。**

---

## 1. 目的

验证 V3 是否真实优于现役 L01，而不是验证它“理论更复杂”。

唯一判据：

> **学员是否更容易完成财富观换轨，并自然进入下一课。**

---

# 2. 六项主测试

## T1｜能 → 贵 → 值 → 我

结课即刻要求学员不看笔记重建：

```text
能 = ?
贵 = ?
值 = ?
我 = ?
```

PASS：能说清因果关系，而不是只记住三本书名。

## T2｜AI 是否仍被理解为“人整体贬值”

问：

> “这堂课是否在说 AI 会让人越来越没价值？”

PASS：回答接近——AI 在重新给能力定价；部分平均能力供给变多，但问题定义、判断、品味、信任、责任等可能更重要。

## T3｜效率 ≠ 方向

给情景：

> “AI 能把一个项目效率提高 10 倍，是否因此证明应该做这个项目？”

PASS：明确区分 HOW 优化与 WHY/价值选择。

## T4｜秘密误解测试

让学员写：

> “秘密是什么？”

FAIL 关键词：内幕、渠道信息差、爆款技巧、别人不知道的小聪明、一次套利。

PASS：接近“值得现实验证的非共识价值候选”。

## T5｜工具完成率

Artifact：`../../exercises/secret-life/L01-AI时代我的价值清算表-v2.md`

目标：

```yaml
in_class_completion_rate_target: ">=80%"
value_candidate_completion_target: ">=70%"
```

## T6｜追课欲

结课问：

> “你现在最想继续追问什么？”

理想自然语言：

- 秘密怎么被市场验证？
- 世界为什么愿意付钱？
- 怎么让别人理解并记住？
- 怎么复制、怎么守住？

如果大量学员直接跳到“我的母体是什么”，说明 L01/L02 handoff 可能失衡。

---

# 3. 认知负荷测试

重点观察 Slide 14“稀缺阶梯”。

记录：

```yaml
cognitive_overload:
  low:
  medium:
  high:
```

如果学员记住“物质→资本→信息…”却说不清“稀缺迁移”，则删减阶梯，不牺牲机制。

---

# 4. 三本书法权测试

问学员：

> “三本书是在证明原力战略正确吗？”

PASS：理解为三种外部理论母根/思想实验，帮助解释时代变化；原力战略是后续对具体生命与事业的回应。

---

# 5. 24h Recall

24 小时后，不看材料回答：

1. AI 首先改变的是什么？
2. 为什么技术不会消灭稀缺？
3. “效率不能证明方向”是什么意思？
4. 新财富公式是什么？
5. 你的 Value Candidate 是什么？

优先看机制重建，不要求逐字。

治理边界：Desktop 阶段只能执行 Context-Isolated Recall Proxy，不得冒充真实 24h Recall。

---

# 6. A/B 对照

V2 与 V3 至少比较：

```text
即时记忆
Recall Proxy / 后续真实24h Recall
秘密误解率
工具完成率
L02 追课欲
时间超支
认知负荷
```

V3 不因“理论更深”自动胜出。

本轮方向性结论：

```yaml
winner_theory_engine: V3
winner_current_live_readiness: V2
v3_should_be_abandoned: false
v3_should_replace_v2_now: false
```

---

# 7. Promotion Gate

```text
READY_NOT_RUN
↓ Desktop Trial
DESKTOP_EVIDENCE_AVAILABLE
↓ 当前裁决：REVISE_BEFORE_LIVE
↓ Human Patch Gate
V3.1 PATCHED SNAPSHOT
↓ Regression
DESKTOP_PASS_SIMULATED
↓ Human Review
LIVE_READY
↓ Live Trial
LIVE_EVIDENCE_AVAILABLE
↓ Real 24h Recall
PROMOTION_REVIEW
↓ Human Ruling
PROMOTED / REVISE / REJECT
```

当前：

```yaml
desktop_trial: EVIDENCE_AVAILABLE_REVISE
context_isolated_recall_proxy: COMPLETE_WITH_ONE_CRITICAL_DRIFT
live_trial: NOT_READY_PATCH_REQUIRED
real_24h_recall: NOT_RUN
promotion: NOT_AUTHORIZED
```
