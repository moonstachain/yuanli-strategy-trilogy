# Trial 09｜G3 五幕真人试讲执行包

```yaml
trial_id: YL-TRILOGY-GENERAL-v2-TRIAL-09-G3-LIVE
status: READY_NOT_RUN
sample_target: 3_to_8
subject: G3_five_act_live_validation
requires_real_learners: true
promotion_effect: none_until_human_gate
```

> 这是 G3 之后唯一真人入口。它不能被 Desktop、AI 模拟、讲师自评替代。

---

# 1. 样本

最低 3 人，推荐 5—8 人。

目标均为未系统学过原力三部曲的小白专家型创业者，样本尽量覆盖：

- 能力很多但高度依赖本人；
- 有产品/收入但价值表达与定位模糊；
- 事业相对成熟、开始出现继承与方向问题。

不得提前发完整定义、答案或工具样例。

---

# 2. 五幕验收主线

G3 后 24h 五幕记忆目标改为：

> **重估 → 入世 → 留存 → 继承 → 定向**

传播层仍可使用“秘密 × 一万倍”，但不再把旧“诞生→入世→寻主→得生→定向”作为默认验收答案。

---

# 3. 每课现场共同记录

## Timing

- 实际总时长：____
- Artifact 独立完成时长：____
- 超时段：____

## One Idea

课后立即闭卷：

> “这一课只改变了你哪一个判断？”

记录原话：____

## Artifact Chain

```yaml
VALUE_THREAD_ID: ______
same_object_as_previous_lesson: Y/N
if_changed_reason: ______
```

若无证据地换对象，链路 FAIL。

## Cliffhanger

不提示下一课内容，问：

> “你现在最自然想继续追问什么？”

只有自然指向下一课危机才 PASS。

---

# 4. 各课核心验收

## L01｜重估

闭卷目标：

- AI 使大量平均能力边际成本下降；
- 真正要经营的是更难被平均化、值得被放大的独特价值；
- 能解释“秘密 × 一万倍”不是信息差套利。

Artifact：选出一个 VALUE_THREAD_ID，不要求证明它正确。

自然问题应接近：

> “它怎样变成世界愿意选择的财富？”

## L02｜入世

闭卷目标：

> **见 → 名 → 繁 → 守**

并能说明：

> 价值不被世界选择，就还不是财富结构。

Artifact：沿用 L01 同一 VALUE THREAD；至少形成一条真实世界选择证据或明确 UNKNOWN。

自然问题应接近：

> **“即使做成了，做完以后到底留下什么？”**

## L03｜留存

新版闭卷目标：

1. **资产，是被保存下来的过去，能够继续为未来做功。**
2. **能力回答我会什么；原力回答因为我在，什么会变得不一样。**
3. **母体是源，原力是力，能力/作品是形，资产是留。**
4. 世界验证成功不自动等于资产形成。

课堂资产卡最低必须独立完成：

- 差异作用 A→B；
- 1条真实证据；
- 1条反证或替代解释；
- 最大本人单点依赖；
- 90天资产化实验。

不要求八格全部精写。

自然问题应接近：

> **“如果这些东西仍只存在我本人身上，怎样让它离开我还能工作？”**

## L04｜继承

闭卷目标：

- OS 不是工具栈；
- 真正规模是高质量判断能被团队/AI在边界内继承；
- 懂/记/判/行是四个器官，“强”是 Outcome→Learning→Reuse 的结果，不是 C5。

Artifact：围绕 L03 的同一个 `FOUNDER_SINGLE_POINT_DEPENDENCY` 建最小控制循环。

必须产生：

```yaml
AMPLIFICATION_TARGET: ______
```

自然问题应接近：

> **“如果系统真的能放大它，这件事值得我放大十年吗？”**

## L05｜定向

闭卷目标：

- 复利不是天然善；
- 成功 / 财富 / 人生回答不同问题；
- 至少给出一条真实不可交换边界；
- 能裁决 AMPLIFICATION_TARGET 是否值得长期放大。

最终形成：

> **《我的原力战略 1.0》v0.1**

---

# 5. 概念混淆测试

课后快速判断：

1. 原力母体就是最强技能。 FALSE
2. 世界愿意付钱就说明完成资产化。 FALSE
3. 用户本人是我的资产。 FALSE
4. 源→力→形→留是新增四个正典模块。 FALSE
5. 知识库很多就等于原力 OS。 FALSE
6. 飞轮是第五种壁垒。 FALSE
7. 原力人生是第四部。 FALSE
8. 复利越多天然越好。 FALSE
9. 世界选择是原力战略不可省略的一环。 TRUE

P0 项 1/2/4/5/6/7 必须全部正确。

---

# 6. 24h Recall

第二天不看资料，依次问：

### Q1 五幕

> 五节课如果只剩五个动作，是什么？

目标：

> **重估 → 入世 → 留存 → 继承 → 定向**

### Q2 一条价值生命史

> 用自己的话解释：一个独特价值怎样从“我看见”走到“值得长期复利”？

要求至少覆盖：世界选择、保存/资产化、继承、方向中的三个。

### Q3 现实变化

> 过去24小时，哪一个真实判断、拒绝、保存或行动已经变化？

“觉得很有启发”不算行为证据。

---

# 7. PASS 判据

单课：

```yaml
timing: <=95min
one_idea_recall: PASS
artifact_minimum_completion: >=80%
value_thread_continuity: PASS
concept_p0_confusion: 0
next_crisis_pull: PASS
```

五课整体：

```yaml
five_act_24h_recall: >=80%
artifact_chainable: >=80%
L03_min_asset_card_completion: >=80%
real_behavior_change_signal: observed_in_majority
```

---

# 8. 失败回写顺序

```text
P0 概念混淆
→ 先删/改定义与边界

P0 工具做不完
→ 先减字段，不加解释

P1 五幕记不住
→ 收敛叙事，不加新口诀

P1 追课欲不足
→ 重写上一课成功制造的下一课危机

P1 VALUE THREAD 断裂
→ 修工具交接，不让每课重新发明案例
```

---

# 9. 当前状态

```yaml
G3_CONVERGENCE: COMPLETE
L03_DESKTOP_REGRESSION: PASS_WITH_OVERLAY
G3_LIVE_TRIAL: READY_NOT_RUN
real_learner_evidence: none_yet
promotion: BLOCKED
```

真人数据完成后，才允许进入新的 Human Gate：

```text
APPROVE_PROMOTION
或
REVISE_AND_RETEST
```