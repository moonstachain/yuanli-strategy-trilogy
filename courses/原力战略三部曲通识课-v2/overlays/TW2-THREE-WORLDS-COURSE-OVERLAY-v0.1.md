# TW2｜Course Three-World Overlay v0.1

> status: `CANDIDATE_LIVE_VALIDATION`
> program: `TW2`
> base_course_pr: `#18`
> frozen_course_head: `9602583c95ae074a72dce840c297a7ce26abd372`
> upstream_tw1_merge: `1553de3d5a8bdceba29ecd89eb4224d4e5626d15`
> canon_effect: `none`
> lesson_rewrite: `false`

## 1. Ruling

TW2 不重写五课，不重排五课，不把 Three Worlds 升级为新的课程正典。

TW2 只验证一个问题：

> **把“源头世界 / 现实世界 / 未来世界”叠加到当前五课后，小白是否更容易理解三部关系、定位自己的问题，并减少关键误解？**

当前 Three Worlds 继续保持：

```text
Canon      = 原力资产 × 原力创业 × 原力OS
Architecture = Source × Venture × Evolution
Worldview  = 源头世界 × 现实世界 × 未来世界
Memory Hook = 回到源头，进入现实，创造未来。
```

## 2. Ontology Order ≠ Learning Journey

正典因果顺序保持：

```text
Source → Reality → Future
A → B → C
```

但当前五课学习顺序不强制改成 A→B→C。

TW2 采用：

```text
L01｜先给世界地图
↓
L02｜先进入现实：一个秘密怎样被世界选择
↓
L03｜回溯源头：为什么这种不同持续从你这里生成
↓
L04｜建设未来：怎样让今天的价值被未来继承
↓
L05｜闭合递归：Source_n → Reality → Future → Source_n+1
```

因此：

> **课程可以从现实切入，但不得反向改写 Canon 因果顺序。**

## 3. Five-lesson overlay

### L01｜原力战略｜只给一张地图

新增的只是 3–5 分钟 Orientation：

```text
源头世界｜什么持续生成我的不同？
现实世界｜世界为什么选择、付费并放大这种不同？
未来世界｜今天发生的价值，怎样被未来继承并继续做功？
```

只要求学员记住：

> **回到源头，进入现实，创造未来。**

禁止在 L01 展开 A1-C4 全部细节。

### L02｜原力创业｜先进入现实世界

课程原结构不变。

Three Worlds 只增加一句定位：

> **你现在进入的是现实世界：一个秘密不是因为你喜欢它就成立，而是要经受时代、用户、心智、模式与竞争的真实选择。**

必须反误解：

```text
现实世界 != 赚钱世界
Revenue = Reality Outcome 的一类
```

### L03｜原力资产｜从现实倒推源头

课程原结构不变。

Three Worlds 只增加一句桥：

> **如果某种价值反复被现实选中，下一问不是“我是什么人格”，而是“什么机制持续从我这里生成这种不同？”**

保持：

```text
原力母体
→ A1 发现母体
→ A2 回到母体
→ A3 获得原力
→ A4 显化原力
→ 原力资产
```

必须反误解：

```text
源头世界 != 人格测试世界
Human Design / MBTI / 星盘 / 荣格 = Source Lens / Evidence Lens
Lens may generate hypotheses; lens may not define the person.
```

### L04｜原力OS｜进入未来世界

课程原结构不变。

Three Worlds 只增加一句定位：

> **未来世界不是预测未来，而是让今天已经发生的身份、知识、判断、行动、结果与学习，在未来任务中被正确继承和复用。**

必须反误解：

```text
未来世界 != AI 世界
未来世界 != 科技趋势
Stored != Reused
Remembered != Compounding
```

### L05｜原力人生｜闭合三世界循环

不把“原力人生”变成第四部。

只让学员完成一次迁移：

```text
我的当前问题主要卡在哪个世界？
→ 对应哪一部？
→ 对应哪个模块？
→ 下一步最小行动是什么？
```

最后闭环：

```text
源头世界_n
→ 现实世界_n
→ 未来世界_n
→ Learning / Reuse
→ 源头世界_n+1
```

## 4. Minimum learner-facing additions

TW2 不要求重写任何 lesson 文件。

课堂上最多增加四类轻量提示：

1. 一张 Three Worlds 总图；
2. 每课一句“你现在在哪个世界”；
3. 每课一个核心反误解；
4. L05 一次 World → Module → Action 导航。

如果这些轻量提示不足以产生理解增益，TW2 应失败，而不是继续向课程塞概念。

## 5. Validation questions

TW2 只验证以下 5 个问题：

1. 学员能否用自己的话说出三个世界？
2. 学员能否把自己的真实问题放进主要世界？
3. 学员能否继续落到 A/B/C 与具体模块，而不是停留在“三个漂亮词”？
4. 三个核心误解是否下降？
5. Three Worlds 是否比旧解释带来净理解增益，而非新增记忆负担？

## 6. Core misconception probes

必须主动观察：

```text
M1｜源头世界 = 人格测试 / 人类图 / 星盘？
M2｜现实世界 = 赚钱？
M3｜未来世界 = AI / Agent / 未来科技？
M4｜三个世界 = 三个新的 Canon Part？
M5｜学习顺序 = 正典因果顺序？
```

## 7. Promotion thresholds

TW2 只有同时达到以下门槛，才值得申请后续 Promotion：

```yaml
correct_three_world_explanation_rate: ">= 0.80"
core_misconception_rate_each: "< 0.20"
self_problem_navigation_rate: ">= 0.70"
canonical_mapping_retained: true
new_parallel_canon_misread_count: 0
```

其中：

- `correct_three_world_explanation_rate`：能说清 Source/Reality/Future 的功能差异；
- `self_problem_navigation_rate`：能把自己的真实问题放到一个主世界，并进一步落到 A/B/C 或模块；
- `canonical_mapping_retained`：仍知道三本正式名称是原力资产 / 原力创业 / 原力OS；
- `new_parallel_canon_misread_count`：任何人明确认为“三个世界是新三部曲正典”，计为 1。

## 8. Evidence model

继续继承 PR #18 的人类友好原则：

```text
L0｜自然证据：课堂自然复述、提问、作业语言
L1｜轻验证：抽样 1–3 人，3–5 个问题
L2｜正式验证：只在准备 Promotion / 强效果声明时启用
```

> **Continuous Passive Evidence + Occasional Active Validation。**

TW2 不要求每位学员填写行政 Ledger。

## 9. Stop conditions

任一成立，暂停 Three Worlds 扩展：

1. 学员仍主要记住旧标签而非三个世界，且理解无提升；
2. “源头=测评”“现实=赚钱”“未来=AI”任一误解持续 >=20%；
3. World 标签不能帮助学员落到 Module / Action；
4. 课程负荷明显上升；
5. 学员开始把 Three Worlds 当成新的 Canon Part。

## 10. Governance boundary

TW2 明确不授权：

```text
Soul Canon change
A1-C4 change
PR #18 merge / promotion
existing lesson rewrite
TW3 Web / Content rollout
TW4 Cross-repo drift guard
runtime action
```

TW2 当前只授权：

> **Overlay + Observation + Evidence Settlement + Human Gate。**
