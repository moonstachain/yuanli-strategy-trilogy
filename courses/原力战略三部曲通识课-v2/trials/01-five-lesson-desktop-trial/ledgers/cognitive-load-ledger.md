# Cognitive Load Ledger｜认知负荷总账

> 当前状态：EMPTY / READY_NOT_RUN

## 采样规则

每个 Session 每 10—15 分钟采样一次 active novel concepts。

```text
1—3 = Green
4—5 = Yellow
6+  = Red
```

| Round | Persona | Lesson | Time window | Active novel concepts | Dropped prior concept | Load color | Evidence | Patch ID |
|---|---|---|---|---:|---|---|---|---|

## 重点观察

不是统计整课出现过多少术语，而是记录：

> 新概念进入工作记忆时，前面的哪个核心判断开始掉线？

## Fail Signals

- 连续两个采样窗口为 Red；
- Learner 只能复述口诀，无法解释因果；
- 出现第二套/第三套记忆编码后第一套明显丢失；
- 工具阶段需要重新讲完整理论才能填写。
