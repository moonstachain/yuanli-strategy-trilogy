# G3 Trial 09｜真人执行 Runbook v1

```yaml
status: READY_TO_RUN_WHEN_REAL_SESSION_EXISTS
issue: moonstachain/yuanli-strategy-trilogy#19
authorized_by: ACCEPT_ROUND2_FOR_TRILOGY_TRIAL
merge_effect: none
promotion_effect: none
```

## A. 开课前 48–2h

1. 确认 3–8 名真实小白专家型创业者；只给匿名编号 P01–P08。
2. 不提前发完整定义、标准答案、PPT 全稿或练习参考答案。
3. 冻结本次使用的 PR #18 head；记录到 `EXECUTION-LEDGER-v1.md`。
4. 为每位学员准备同一个 `VALUE_THREAD_ID` 连续加工，不允许五课换五个对象。
5. 确认 24h Recall 可在课程结束约 24h 后联系到参与者。
6. 课程只使用已冻结材料；现场如发现 P0 问题，记录，不临时新增一级概念救场。

## B. 现场

每课必须记录：

```text
actual timing
→ one idea closed-book recall
→ artifact completion
→ VALUE_THREAD continuity
→ concept confusion
→ natural next-crisis question
```

L03 额外看：

- 资产 ≠ 收入/结果/资源；
- 原力 ≠ 技能/能量感；
- 世界验证 ≠ 已完成资产化；
- “留下来”是否自然制造 L04 问题。

L04 额外看：

- 时间 ≠ 自动复利；
- 能否举出时间熵；
- `Continuity × Adaptation`；
- C1–C4 = Normative / Epistemic / Policy / Reality；
- `Output ≠ Action ≠ Outcome ≠ Learning ≠ Reuse`；
- `Retrieval ≠ Reuse`；
- 能否完成真实 `State_t → State_t+1`。

## C. 课程结束 0–1h

1. 立刻补齐匿名 Live Ledger。
2. 不给 24h Recall 提前发答案。
3. 为每位完成全程的学员记录真实 `session_end_at` 和 `24h_recall_due`。
4. 立即状态只能是：

```text
LIVE_COMPLETED_WAITING_24H_RECALL
```

不得写 PASS / reusable / compounding。

## D. 约 24h

逐人按 `24H-RECALL-LEDGER-v1.md` 原问题执行：

1. 五幕；
2. 独特价值的完整生命史；
3. 为什么经营十年不等于十年复利；
4. 自己的一条 Reality → Learning → next Task change；
5. 过去24h真实行为变化。

不得提示关键词。

## E. Behavior Change

把“有启发”排除，只记录：

```text
DEC_CHANGE
REJECT_CHANGE
SAVE_CHANGE
ACT_CHANGE
PRELOAD_CHANGE
NO_CHANGE
```

如果声称 Reuse，必须满足：真实独立 Task2、决策前 preload、actual use、DEC/WPK/ACT 至少一项真实改变。

## F. Evidence Settlement

填 `EVIDENCE-SETTLEMENT-TEMPLATE-v1.md`。

机器结算只允许：

```text
PASS_FOR_FRESH_HUMAN_GATE
REVISE_AND_RETEST_RECOMMENDED
INCOMPLETE_EVIDENCE
FAIL_SAFE
```

随后停止，等待 Fresh Human Gate：

```text
APPROVE_PROMOTION
or
REVISE_AND_RETEST
```

## G. Fail closed

出现以下任一项，停止 Promotion：

- 少于 3 名真实合格参与者；
- 用 AI/Desktop 补真人数据；
- 24h Recall 被提前泄题；
- P0 概念混淆未清零；
- C1-C4 被理解成四类新资产；
- Retrieval 被当作 Reuse；
- Evidence 不足却试图 merge/promotion。
