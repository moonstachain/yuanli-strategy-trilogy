# Trial 10｜Observer Rubric

## 1. 观察原则

观察者只能记录，不得提示、教学、补救或暗示标准答案。若观察者介入改变学员回答，该条记录标记 `CONTAMINATED`。

## 2. 八态评分

每态只允许：

```text
0 = NOT_OBSERVED
1 = PARTIAL / AMBIGUOUS
2 = CLEARLY_OBSERVED
X = NOT_RUN / NOT_APPLICABLE
```

### 唤

问：学员是否先显性表达自己的 M0？

强证据：自发原话、实际选择、下注。
弱证据：从老师给的两个选项中随便选。

### 裂

问：学员是否明确发现原模型解释不了某个事实？

强证据：能复述“我原来认为 X，但 Y 使我发现 X 不够”。
禁止：把惊讶、笑声、沉默直接记为裂。

### 聚

问：学员能否把困惑压成一个真实问题？

强证据：不提示时提出与本课母问题结构一致的问题。

### 构

问：学员是否在老师给正式定义前尝试过候选解释？

记录：`self_generated | prompted_generation | teacher_given_only`。

### 辨

问：是否能通过近邻反例、边界例、P0 混淆题？

强证据：不仅选对，还能解释为什么。

### 生

问：是否能把新模型用于自己的真实 VALUE THREAD 并产生 Artifact？

强证据：对象真实、字段可检查、不是抄示例。

### 迁

问：课堂未讲过的新场景中能否正确使用深层结构？

T0 若无陌生迁移任务，记录 `NOT_RUN`，不得推断。

### 化

问：新模型进入真实行动/Outcome 后是否被强化、修订或否定？

通常 T+30d 才有资格记录；课堂内不得提前 PASS。

## 3. 七证记录

```yaml
hit:
  state: 0|1|2|X
  quote:
discriminate:
  state: 0|1|2|X
  evidence:
retrieve:
  state: 0|1|2|X
  verbatim_recall:
self_map:
  state: 0|1|2|X
  real_object:
use:
  state: 0|1|2|X
  artifact:
transfer:
  state: 0|1|2|X
  new_case:
writeback:
  state: 0|1|2|X
  decision_action_outcome:
```

## 4. 观察者必须记录的原话

每课至少保留：

1. 一条 M0 原话；
2. 一条认知失配原话；
3. 一条课后 M1 原话；
4. 一个最大误解；
5. 一个最自然的下一问题。

## 5. 失败也必须保留

以下全部属于高价值 Evidence：

- 学员没有被击中；
- 裂与聚无法区分；
- 学员只会背口诀；
- Artifact 靠老师救援；
- 7d 完全不能迁移；
- 30d 没有现实使用；
- 学员现实反证课程模型。

不得只回写成功样本。
