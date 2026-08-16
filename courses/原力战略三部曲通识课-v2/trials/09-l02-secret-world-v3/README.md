# Trial 09｜L02「一个秘密，凭什么变成财富？」V3 Candidate

```yaml
trial_id: YL-L02-V3-TRIAL-09
candidate_id: YL-TRILOGY-GENERAL-v2-L02-V3-CANDIDATE
status: READY_NOT_RUN
evidence_class: simulated_desktop_trial
real_learner_evidence: false
promotion_authority: human
canon_effect: none
```

## 1. 目的

验证 V3 是否比现役 L02 更能把学员从“好点子/风口/定位/扩张/护城河”的旧创业语言，迁移到四次现实选择：

> **见 → 名 → 繁 → 守**

本轮先做 P01-P06 红队。只有四类关键误解全部清零，才允许与现役 L02 做方向性 Desktop A/B。

---

# 2. 冻结规则

Trial 开始前冻结：

- Lesson V3 Candidate；
- 90min Director V3；
- 22页 Deck Blueprint V3；
- 《我的秘密入世四关卡 V2》；
- 复用的 L02 Evidence Packet v1。

运行中不得修改冻结资产。

发现问题只写 Patch Candidate；若有 P0/P1 blocker，则 A/B 暂停。

---

# 3. Learner Blindness

沿用现有 P01-P06 Persona 契约：

```yaml
prior_yuanli_knowledge: none_or_existing_persona_contract
access_to_author_intent: false
fake_understanding: prohibited
expose_confusion: true
use_only_seen_content: true
```

P06 继续作为 regression/reference persona，不冒充真实学员。

---

# 4. 四类必攻误解

## M1｜风口化

错误：

> 见 = 找 AI / 银发 / 出海等热门机会。

PASS：

> 能主动区分“外部机会”与“对结构变化形成的非平均判断”，并写出 Why Now Thesis。

## M2｜起名化

错误：

> 名 = 起一个新词、做差异化定位、换一句 slogan。

PASS：

> 能说出旧分类、比较对象、判断标准如何被改变，并形成 Category Thesis。

## M3｜规模化

错误：

> 繁 = 多卖、多招人、多渠道、自动化率越高越好。

PASS：

> 能定义自己的最小复制单元与 Founder Bottleneck，说明哪一份价值不再需要本人重新制造。

## M4｜护城河化

错误：

> 守 = 别人绝对抄不了 / 专利越多越安全 / 飞轮是第五壁垒。

PASS：

> 只使用虚实入出，并能说明一次交易后的 Asset Delta。

---

# 5. 接口 Gate

必须验证：

> **L01 V3.1 的 Value Candidate 不得被 L02 偷换为“已经被现实验证的秘密”。**

PASS 语言：

> 第二课是在继续验证并让它进入财富结构，而不是宣告它已经成立。

---

# 6. Artifact Gate

目标：

```yaml
estimated_completion_time: "<=11min"
quality: L3
same_value_candidate: required
one_30d_gate_only: required
```

失败条件：

- 四关都写成抽象口号；
- 没有证据/反证；
- 最后圈多个主瓶颈；
- 见写赛道、名写 slogan、繁写扩张、守写“别人不能抄”。

---

# 7. Handoff Gate

结课第一自发下一问应主要指向 L03：

> **为什么同样面对这些变化，偏偏是我更容易形成这个判断？**

至少 `5/6` Persona 的第一自然追问应指向生成源/为什么是我，而不是回头追问四关枝节。

---

# 8. Recall Proxy

Desktop 阶段只允许 Context-Isolated Recall Proxy，不得冒充真实 24h Recall。

固定五问：

1. 见为什么不是找风口？
2. 名为什么不是起名字？
3. 最小复制单元是什么？
4. 守为什么不是“别人做不了”？
5. 你未来30天只验证哪一关？为什么？

---

# 9. A/B Gate

只有以下全部通过才允许运行 V2 vs V3 方向性 Desktop A/B：

```yaml
critical_misconception_recurrence: 0
interface_drift: 0
artifact_L3: 6/6
artifact_time: <=11min
handoff: >=5/6
canon_boundary_breach: 0
```

A/B 比较：

- 四误解清晰度；
- L01→L02 接口严谨性；
- 工具行动性；
- 认知负荷；
- 90min 时间风险；
- L03 追课欲；
- 正典边界。

V3 不因“更新”自动胜出。

---

# 10. 状态机

```text
READY_NOT_RUN
→ freeze V3 snapshot
→ P01-P06 red team
→ misconception gate
→ recall proxy
→ if PASS: V2/V3 A-B
→ Trial 09 ruling
→ Human Gate
→ LIVE_TRIAL_READY / REVISE / REJECT
```

当前：

```yaml
red_team: NOT_RUN
recall_proxy: NOT_RUN
ab: BLOCKED_UNTIL_RED_TEAM_PASS
live_trial: NOT_AUTHORIZED
promotion: NOT_AUTHORIZED
```
