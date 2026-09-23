# Trial 09｜Human-Friendly Progressive Evidence Protocol v1

```yaml
status: ACTIVE_OVERLAY
adopted_at: 2026-08-18
trigger: facilitator_feedback_on_human_friction
human_gate_context: ACCEPT_ROUND2_FOR_TRILOGY_TRIAL
supersedes_mandatory_full_recall: true
keeps_formal_ledgers_available: true
merge_effect: none
promotion_effect: none
```

> 这份 Overlay 只改变“如何取证”，不降低“什么声明需要什么证据”的标准。
>
> 核心原则：**后台严谨，前台低摩擦。人类负责真实授课与自然反馈，系统负责尽量留下证据。**

---

# 1. 当前 Trial 的真实目标

本轮首先验证：

> **新版 L03→L04 解释是否在真实小班中获得可理解、可接受、值得继续使用的现实信号。**

它不是一次临床试验，也不是为了证明普遍因果效果。

因此，不再要求 5 名学员全部完成固定五问、逐项 Ledger 和逐人 Behavior Change 证明。

---

# 2. Progressive Evidence

## L0｜自然证据｜默认

不让讲师或学员额外填表。

可接受：

- 真实课堂发生；
- 人数 / 时长；
- 讲师对课堂整体反应的自然观察；
- 学员自然提问、复述、课后聊天、作业、后续主动引用；
- 后续真实行动中自然出现的概念使用。

L0 可支持：

```text
REAL_SESSION_OCCURRED
INITIAL_ACCEPTANCE_SIGNAL
WORTH_CONTINUING
```

L0 不支持：

```text
CAUSAL_EFFECT_PROVEN
REUSE_PROVEN
COMPOUNDING_PROVEN
CANON_PROMOTION
```

## L1｜轻验证｜按需、抽样

只有当需要消除关键不确定性时，对 1–2 名自然可接触学员问一两个问题即可。

推荐问题：

> “昨天那堂课，到现在你脑子里还剩下什么？”

可选第二问：

> “有没有哪个真实判断因为这堂课变了？”

不要求逐字标准答案，不要求结构化表格；AI / OS 负责从自然回答中提取：

- 是否还记得时间不自动复利；
- 是否理解资产→OS / 留下来≠复利；
- 是否出现真实判断迁移。

## L2｜正式验证｜只在高声明时

只有准备：

- Canon Promotion；
- 对外宣称课程效果；
- 大规模复制；
- 证明真实 Reuse / Compounding；

才启用现有完整：

```text
24H-RECALL-LEDGER
BEHAVIOR-CHANGE-LEDGER
EVIDENCE-SETTLEMENT
Task2 preload / actual use
```

原有 Ledgers 保留，身份从“日常必填”降为“L2 Formal Validation 工具”。

---

# 3. Current Session Settlement｜2026-08-18

已知自然证据：

```yaml
real_session_occurred: true
participant_count: 5
reported_duration_min: 120
reported_approx_end: 2026-08-18T12:00:00+08:00
immediate_acceptance_signal: POSITIVE
source: facilitator_user_attestation
```

因此当前允许的最强结论：

```text
L0_COMPLETE
INITIAL_REALITY_SIGNAL_POSITIVE
WORTH_CONTINUING_IN_LIVE_USE
```

不要求 2026-08-19 12:00 对 P01–P05 全员执行固定 Recall。

如果后续自然接触到 1–2 名学员，可以顺手做 L1；如果没有，也不制造额外人类任务。

---

# 4. Human Effort Budget

Trial 设计约束：

```text
新增一项取证动作前，先问：
这项动作会显著改变当前决策吗？
```

如果答案是否定：

> **不增加人类步骤。**

课程研发默认使用：

```text
Continuous Passive Evidence
+
Occasional Active Validation
```

而不是每场课都做完整实验。

---

# 5. Fresh Human Gate 何时触发

只有以下任一情况发生，才值得再次正式 Review：

1. 连续多场真实课堂出现一致正向 / 负向信号；
2. 自然出现 1–2 条强 L1 认知迁移证据；
3. 出现真实行为变化或主动复用；
4. 准备把该解释升级为正式课程默认 / Canon；
5. 出现 P0 概念冲突，需要回写理论。

机器可形成：

```text
CONTINUE_OBSERVING
READY_FOR_LIGHT_REVIEW
READY_FOR_FORMAL_VALIDATION
REVISE_FROM_REALITY
```

未经新 Human Gate，不 merge / promotion。

---

# 6. 一句话产品纪律

> **好的课程 OS，不让讲师为了证明课程有效而多做一套行政工作；它应该从真实教学本身获得足够证据。**
