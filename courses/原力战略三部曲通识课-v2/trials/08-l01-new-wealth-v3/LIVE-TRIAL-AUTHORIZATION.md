# L01 V3.1｜真人试讲授权

```yaml
authorization_id: YL-L01-V3.1-LIVE-AUTH-20260816
candidate: YL-TRILOGY-GENERAL-v2-L01-V3.1-CANDIDATE
status: AUTHORIZED_READY_NOT_RUN
authorized_at: 2026-08-16
authority_basis:
  - Human Patch Gate APPROVED
  - V3.1 frozen snapshot
  - Persona regression PASS
  - Context-Isolated Recall Proxy PASS
canon_effect: none
promotion_effect: none
```

## 1. 授权对象

真人试讲必须使用冻结快照：

```text
branch: snapshot/l01-v3.1-20260816
sha: eda55d3d653c03ba2c3b78822745e80f1b9b10f3
```

执行资产：

- Lesson：`lessons/secret-life/L01-秘密诞生-原力战略-v3.1-candidate.md`
- Director：`director/secret-life/L01-90MIN-DIRECTOR-v3.1-candidate.md`
- Deck：`deck/secret-life/01-原力战略-AI时代新财富算法-PPT蓝图-v3.1.md`
- Artifact：`exercises/secret-life/L01-AI时代我的价值清算表-v3.1.md`

试讲期间不得边讲边改冻结稿；发现问题只进入 Live Ledger。

---

# 2. 真人试讲唯一目标

不是证明“理论很深”，而是验证：

> **真实小白学员能否在 90 分钟内完成财富观换轨，并自然产生进入 L02 的问题。**

---

# 3. 必测 Gate

## G1｜四字机制 Recall

结课闭卷：

```text
能 = ?
贵 = ?
值 = ?
我 = ?
```

记录：完整 / 部分 / 失败。

## G2｜秘密误解

问：

> “一个很好的 AI 商业机会，是不是就等于你的秘密？”

PASS 必须区分：

```text
机会 = 外部窗口
秘密 = 对窗口形成、愿意交给现实验证的非平均判断
```

## G3｜Artifact

记录：

```yaml
median_completion_time:
L3_completion_rate:
value_candidate_completion_rate:
```

目标：

```yaml
median_completion_time: "<=12min"
L3_completion_rate: ">=70%"
value_candidate_completion_rate: ">=80%"
```

## G4｜使命化

观察 Value Candidate 是否被理解为“终极使命 / 一生唯一目标”。

目标：`critical_missionization = 0`。

## G5｜L02 Handoff

结课只问：

> “你现在最想继续解决的下一个问题是什么？”

目标：至少 70% 第一自发问题指向市场理解、付费、品类、复制或壁垒。

## G6｜90min Timing

逐段记录真实时间。不得用导演计划时间冒充实测。

---

# 4. 24h Recall

真人试讲结束约 24 小时后，不提供材料，重新回答：

1. AI 首先改变的是什么？
2. 为什么技术不会消灭稀缺？
3. 为什么效率不能证明方向？
4. 机会和秘密有什么区别？
5. 你的 Value Candidate 是什么？为什么它不是唯一使命？
6. 你准备让哪一次输出成为下一次输入？

这一轮才允许写入：

```yaml
real_24h_recall: measured
```

---

# 5. V2 / V3.1 真人 A/B

如果有条件，使用相似学员样本分别走 V2 与 V3.1，至少比较：

```text
开场抓取力
核心机制重建
秘密误解率
认知负荷
Artifact 完成率与时间
L02 追课欲
24h Recall
```

V3.1 不因 Desktop PASS 自动获得最终胜利。

---

# 6. Live 后状态

真人试讲一结束，只允许进入：

```text
LIVE_EVIDENCE_AVAILABLE
```

必须等待真实 24h Recall 后，才能进入：

```text
PROMOTION_REVIEW
```

未经 Human Promotion Ruling，不得：

- 替换 V2；
- 宣告 `validated_live`；
- 合并为唯一主课；
- 修改 Soul 正典。
