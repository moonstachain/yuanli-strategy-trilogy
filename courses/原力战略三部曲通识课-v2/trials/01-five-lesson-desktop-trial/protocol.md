# Protocol｜五课 Desktop Trial v1

## 0. 试验性质

Desktop Trial 是课程发布前的模拟压力测试，不等于真实课堂证据。

任何结果必须标记为：

```yaml
evidence_class: simulated_desktop_trial
real_learner_evidence: false
```

不得把 Context-Isolated Recall 冒充真实 24 小时回忆；不得把模拟工具完成时间冒充真人课堂计时。

## 1. 冻结规则

Round 1 唯一课程输入：

`6be729bf56759604f2ce2ff19e5163e2206ae2cf`

冻结对象：

- lessons/01—05；
- exercises/五张主工具；
- deck/01—05。

Round 1 全部 Session 结束前，Editor 不得修改冻结对象。

发现问题只写入 Ledger 与 Patch Candidate。

## 2. Learner Blindness Contract

```yaml
prior_yuanli_knowledge: none
access_to_soul_canon: false
access_to_future_lessons: false
access_to_project_memory: false
infer_author_intent: prohibited
ask_when_confused: required
fake_understanding: prohibited
```

Learner 只能使用：

1. 当前 Persona；
2. 已经在本次纵向学习中真正学过的内容；
3. 自己此前完成的课程工具与笔记。

## 3. Teacher Contract

Teacher 必须：

- 使用冻结稿；
- 遵守当前课 90 分钟 Run of Show；
- 不提前泄露后续课程答案；
- 不因 Learner 卡住而增加冻结稿之外的大段新理论；
- 允许用冻结稿已有案例、定义和追问澄清。

若必须临时新增解释才能继续：

> 记录为 `teacher_rescue_required: true`，本身就是课程缺陷证据。

## 4. Observer Contract

Observer 只能记录：

- comprehension_breakpoint；
- misconception；
- attention_drop；
- load_peak；
- tool_block；
- timing_risk；
- teacher_rescue；
- narrative_handoff。

不得替 Learner 解释，不得在 Session 中提出 Patch。

## 5. Examiner Contract

每课结束执行固定闭卷五问：

1. 不用原句，这一课到底改变了你什么判断？
2. 它最容易被误解成什么？为什么不是？
3. 这跟你现在最具体的一个事业问题有什么关系？
4. 接下来你准备验证什么？
5. 你现在最想继续解决的下一个问题是什么？

## 6. Red Team Contract

### L01 必攻

- AI 要淘汰人；
- 要找一个 AI 不会的技能；
- 秘密 = 商业机会；
- 只有你 = 天选之人。

### L02 必攻

- 见 = 追风口；
- 名 = 起名字；
- 繁 = 多卖；
- 守 = 别人抄不了；
- 飞轮 = 第五壁垒。

### L03 必攻

- 母体 = 天赋；
- 母体 = MBTI；
- 母体 = 兴趣；
- 母体 = 职业优势；
- Mother Hypothesis 一次找到后永久不变。

### L04 必攻

- OS = 软件；
- OS = 知识库；
- OS = Agent；
- C3 = 思维导图；
- 强 = C5。

### L05 必攻

- 原力人生 = 第四部；
- 人生 = 唯一使命；
- 长期主义 = 永远做一件事；
- 终局 = 财富自由。

## 7. 工具质量等级

```text
L0 空白 / 无法完成
L1 能填，但多为抽象标签
L2 有具体事实与个人映射
L3 有事实 + 判断 + 取舍 + 可验证行动
```

只有 L3 算通过。

目标 Desktop Time Budget：

- L01 起点图：≤13min
- L02 秘密四步卡：≤15min
- L03 母体假设卡：≤15min
- L04 OS一页架构：≤15min
- L05 原力人生一页纸：≤14min

Desktop 只能记录 `estimated_completion_time`。

## 8. Cognitive Load Ledger

每 10—15 分钟检查一次 active novel concepts：

```text
1—3 = Green
4—5 = Yellow
6+  = Red
```

重点不是概念总数，而是：

> 新概念出现时，前面哪个主判断开始从工作记忆中掉线？

## 9. Narrative Handoff Gate

理想自然问题：

- L01→L02：秘密到底怎么找、怎么变成钱？
- L02→L03：为什么偏偏是我能看见？
- L03→L04：如果我的原力越来越值钱，怎样避免本人被绑死？
- L04→L05：如果什么都能被放大，我究竟应该放大什么？

若 Learner 的自发下一问主要指向课内枝节，则 Handoff 降级。

## 10. Patch Governance

Round 1 结束前禁止修改正文。

问题分级：

- P0：核心误解 / 法权漂移 / 会导致错误行动；
- P1：明显负荷、节奏、工具阻塞；
- P2：表达、案例、视觉与顺滑度优化。

所有 Patch 必须形成：

`Misconception → Evidence → Root Cause → Minimal Patch → Regression Test`

## 11. Round Gates

### Round 1 完成条件

- P01/P02/P03 × L01—L05 = 15 Sessions 完整；
- 四类 Ledger 已汇总；
- 五课 reconstruction 已执行；
- 没有在中途修改冻结课程。

### Round 2 授权条件

Round 1 完成并人工查看原始证据后，才允许 P04/P05 + Red Team。

### Round 3 授权条件

- P0/P1 Patch 已裁决并应用；
- 创建全新 Persona F；
- 重新冻结 patched snapshot。

## 12. 进入 Live Trial 的最低门槛

必须同时满足：

1. 三位纵向 Persona 均能重建五课龙骨；
2. Critical Misconception = 0；
3. 五张工具全部达到 L3；
4. Handoff = 4/4 PASS；
5. 新 Persona F Regression PASS。

通过后只允许：

```yaml
desktop_trial: pass
live_trial: ready_not_run
reusable: false
supersedes_v1: false
```
