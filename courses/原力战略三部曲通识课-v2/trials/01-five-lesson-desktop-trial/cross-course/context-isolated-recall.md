# Context-Isolated Recall｜隔离回忆代理测试

> 当前状态：READY_NOT_RUN

## 目的

严格测试课程记忆是否依赖当前上下文残留。

本测试是 **Desktop Proxy**，不是真实 24 小时回忆。

必须标记：

```yaml
evidence_class: simulated_context_isolated_recall
real_24h_memory_test: false
```

## 执行方法

为每位 P01/P02/P03 创建一个全新 Learner Context。

新 Context 只能获得：

1. Persona 文件；
2. Learner 自己在上一 Context 中写下的课程笔记；
3. Learner 自己完成的五张工具。

不得获得：

- 五课课程正文；
- Deck；
- Soul；
- Observer Notes；
- Examiner 标准答案；
- 本项目历史记忆。

## 问题

1. 你还记得原力战略最核心讲什么吗？
2. 五课你分别记得什么？
3. “秘密”是什么，不是什么？
4. 母体是什么，不是什么？
5. 原力 OS 与知识库/Agent 的区别是什么？
6. 原力人生为什么不是第四部？
7. 你真正准备采取的下一步行动是什么？

## 重点观察

- 记住的是主判断还是术语碎片；
- 记忆是否发生危险变形；
- 五套记忆编码是否互相干扰；
- Learner 自己的工具是否足以恢复课程主线。

## 常见危险变形

- 母体 → 天赋/人格；
- 秘密 → 信息差；
- 一万倍 → 流量规模；
- OS → AI工具栈；
- 原力人生 → 使命愿景或第四部。

## Result Template

```yaml
persona: TBD
core_judgment_recall: NOT_RUN
misconception_after_isolation: []
five_lesson_order_recall: NOT_RUN
action_recall: NOT_RUN
overall: NOT_RUN
```
