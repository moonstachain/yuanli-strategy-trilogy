# TW2 Three Worlds｜Observation Rubric v0.1

> status: `READY_NOT_RUN`
> evidence_priority: `L0_NATURAL_FIRST`

## A. Explanation quality

对每个被观察到的学员，只在有自然证据或 L1 抽样时记录。

### E0｜未形成

- 说不出三个世界；或
- 只记得词，无法区分功能。

### E1｜记得标签

能说出“源头 / 现实 / 未来”，但解释仍模糊。

### E2｜功能正确

至少能表达：

```text
源头：什么持续生成我的不同
现实：世界怎样选择 / 检验 / 放大这种不同
未来：今天的价值怎样被未来继承与复用
```

### E3｜能迁移

能用自己的案例解释三个世界，而不是背定义。

`correct_three_world_explanation` 计数规则：E2 或 E3 = true。

## B. Navigation quality

### N0｜不能定位

无法判断自己的真实问题主要属于哪个世界。

### N1｜World only

能放进一个主世界，但不能继续下钻。

### N2｜World → Book

能落到：

```text
源头 → 原力资产
现实 → 原力创业
未来 → 原力OS
```

### N3｜World → Module → Action

还能进一步落到 A1-C4 某模块，并给出一个下一步行动。

`self_problem_navigation` 计数规则：N2 或 N3 = true。

## C. Canon retention

合格至少同时知道：

1. 三本正式名称仍是 `原力资产 / 原力创业 / 原力OS`；
2. Three Worlds 是帮助理解三部关系的世界观表达；
3. 原力人生不是第四部。

## D. Misconception flags

每个 flag 独立记录 `true / false / not_observed`。

### M1｜Source-as-test

错误表现：

> “源头世界就是找 MBTI / 人类图 / 星盘，看我是什么类型。”

### M2｜Reality-as-money

错误表现：

> “现实世界就是赚钱、变现。”

### M3｜Future-as-AI

错误表现：

> “未来世界就是 AI、Agent、未来科技。”

### M4｜Parallel-canon

错误表现：

> “原力战略现在正式改成源头世界、现实世界、未来世界三部。”

### M5｜Journey-equals-ontology

错误表现：

> “因为课程先讲创业，所以正典因果顺序也是 Reality → Source → Future。”

## E. Net comprehension signal

观察者最后只做一个低推断裁决：

```text
CLEAR_GAIN
NO_MATERIAL_GAIN
ADDED_LOAD
AMBIGUOUS
```

定义：

- `CLEAR_GAIN`：Three Worlds 明显帮助解释、导航或纠错；
- `NO_MATERIAL_GAIN`：记住了新词，但没有更会判断；
- `ADDED_LOAD`：增加认知负担或与旧标签竞争；
- `AMBIGUOUS`：证据不足。

## F. No coaching rule

验证时不得：

- 用标准答案提示学员；
- 因为学员说错而立即重新讲一遍再计正确；
- 把讲师自己的判断当学员证据；
- 把“点头 / 觉得有道理”当正确理解。
