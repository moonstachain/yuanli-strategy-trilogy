# G3 Trial 09｜24h Recall Ledger v1.1

```yaml
trial_id: YL-TRILOGY-GENERAL-v2-TRIAL-09-G3-LIVE
status: L2_FORMAL_VALIDATION_TOOL_NOT_REQUIRED_FOR_CURRENT_CLAIM
session_end_at_approx: 2026-08-18T12:00:00+08:00
original_recall_target_at_approx: 2026-08-19T12:00:00+08:00
mandatory_for_all_participants: false
pre_answering_forbidden: true
```

> 本 Ledger 保留用于 L2 正式验证，但不再要求 2026-08-19 12:00 对 P01–P05 全员执行固定 Recall。
>
> 当前 Trial 的最小声明只是：真实课堂已发生、出现初步正向接受信号、值得继续真实使用。这个声明由 L0 自然证据即可支持。

## 什么时候使用本 Ledger

只有准备进行以下高强度声明时才启用：

- Canon Promotion；
- 对外宣称课程效果；
- 大规模复制前的正式验证；
- 需要证明稳定认知留存；
- 需要证明真实 Behavior Change / Task2 Reuse。

## L1 轻验证优先

如果只是想知道“学员第二天还剩下什么”，优先抽样 1–2 名自然可接触学员，仅问：

> **昨天那堂课，到现在你脑子里还剩下什么？**

必要时再问：

> **有没有哪个真实判断因为这堂课变了？**

AI / OS 负责把自然回答结构化；不要求讲师手工填完整 Ledger。

---

# L2 Formal Recall Template

只有 L2 被显式触发时，才使用以下模板。

## P__ Recall

```yaml
pid: P__
session_end_at: NOT_OBSERVED
recall_started_at: NOT_OBSERVED
elapsed_hours: NOT_OBSERVED
materials_visible: false
teacher_prompt_beyond_frozen_questions: false
```

### Q1｜五幕

问题：五节课如果只剩五个动作，是什么？

原话摘要：______

```yaml
five_act_recall: NOT_OBSERVED
```

### Q2｜价值生命史

问题：一个独特价值怎样从“我看见”走到“值得长期复利”？

原话摘要：______

```yaml
world_selection_present: NOT_OBSERVED
assetization_present: NOT_OBSERVED
os_learning_present: NOT_OBSERVED
direction_present: NOT_OBSERVED
```

### Q3｜时间为何不自动复利

问题：为什么一家经营十年的公司，可能并没有拥有十年的复利？

原话摘要：______

```yaml
time_entropy_understood: NOT_OBSERVED
```

### Q4｜State Transition

问题：举一个你自己的例子——过去一次真实经历，下一次应该因此怎样不同？

```text
Reality / Outcome：______
Learning：______
Next Task：______
Decision / Action change：______
```

```yaml
state_transition_real_example: NOT_OBSERVED
```

### Q5｜真实变化

问题：最近哪一个真实判断、拒绝、保存或行动因为这套课程发生变化？

原话摘要：______

```yaml
behavior_change_claimed: NOT_OBSERVED
behavior_change_evidence_ref: NOT_OBSERVED
```

## Recall integrity

```yaml
answer_leakage: NOT_OBSERVED
teacher_rescue: NOT_OBSERVED
participant_independent: NOT_OBSERVED
```

## Participant recall verdict

只允许：

```text
PASS
PARTIAL
FAIL
INVALID
NOT_RUN
```

默认当前：`NOT_RUN`，这不是失败，而是 **L2 未被当前声明触发**。
