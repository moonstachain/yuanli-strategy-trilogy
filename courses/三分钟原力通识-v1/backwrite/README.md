# Evolution Note 与回写协议

发布结果只能先成为课程学习证据，不能自动升级 Soul 正典。

## 回写链路

```text
正式发布
→ 24h / 72h / 7d 观察
→ 用户复述、误解、案例、行动与结果
→ 形成 Evolution Note
→ 提出课程修改或 Soul 候选
→ Human Gate
→ 下一期或下一任务明确加载
→ 复用结果
```

## Evolution Note 最小字段

```yaml
note_id:
episode_id:
observation_window:
audience_sample:
what_was_understood:
misunderstandings:
user_language:
real_actions:
outcomes:
failed_cases:
changed_rule:
change_target: script | lesson_card | domain_pack | course_protocol | soul_candidate
human_decision:
next_task_loading_point:
reuse_evidence:
```

## 三种回写等级

### L1｜内容修订

修改标题、例子、语言、节奏或机制图，不改变课程规则。

### L2｜课程协议候选

修改模型进入标准、授课结构、练习或验收方法，需要课程负责人批准。

### L3｜Soul 正典候选

只有当真实结果反复显示现有正典边界需要调整时，才提出候选；必须独立 PR、证据账本与人工裁决。

## 复利判据

仅有一条“学到了什么”不构成复利。

至少需要：

```text
Task1 产生一条规则
→ 规则获批
→ Task2 开始前明确读取
→ Task2 行动或结果发生可观察变化
```

没有第二次真实加载，状态保持 `evolution_noted`，不得标记 `reusable`。
