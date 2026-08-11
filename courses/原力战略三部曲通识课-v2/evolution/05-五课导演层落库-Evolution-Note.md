# Evolution Note 05｜五课 Director Layer 落库

## 1. 触发原因

在 1+3+1 五课结构完成 Desktop Trial Round 1—3、Human Patch 与 Persona F Regression 后，课程已经具备稳定结构；随后新增 Narrative Layer，解决“为什么学员愿意一路追下去”。

本轮继续解决第三个问题：

> **同一套结构与叙事，如何在真实90分钟课堂里被导演出来？**

因此建立独立 Director Layer。

---

## 2. 三层架构

```text
Structure Layer
讲什么
↓
Narrative Layer
为什么愿意一路追
↓
Director Layer
这一分钟课堂发生什么
```

三层不得混淆。

### Structure Layer

- 五课知识结构；
- 五张工具；
- 关键概念边界；
- patched snapshot：`e05450f800b47ff0360c75cb73365e2011d7ee69`；
- 已通过 simulated Desktop Regression。

### Narrative Layer

- 一万倍机器；
- 五幕危机升级；
- 三个叙事符号；
- 六段叙事协议；
- post-desktop candidate；
- 尚未被真人课堂验证。

### Director Layer

- 逐分钟节奏；
- 黑屏、停顿、追问、案例、工具、闭卷与 Cliffhanger；
- 教师何时不解释；
- 每课情绪曲线；
- Live Trial 观察点；
- post-desktop candidate；
- 尚未被真人课堂验证。

---

## 3. 新增文件

```text
director/
├── README.md
├── L01-原力战略-导演脚本.md
├── L02-原力创业-导演脚本.md
├── L03-原力资产-导演脚本.md
├── L04-原力OS-导演脚本.md
└── L05-原力人生-导演脚本.md
```

---

## 4. 五课情绪曲线

### L01｜原力战略

> 自信 → 不安 → 旧财富算法失效 → 醒来 → 对号 → 追问

课尾：

> **你看见秘密以后，凭什么变成财富？**

### L02｜原力创业

> 兴奋 → 受阻 → 四次变形 → 放大 → 警觉 → 追根

课尾：

> **同样的世界，为什么偏偏是你更容易看见？**

### L03｜原力资产

> 剥离 → 困惑 → 破案 → 取舍 → 验证 → 新危机

课尾：

> **如果最值钱的判断只在你脑中，你拥有事业还是事业拥有你？**

### L04｜原力OS

> 成功 → 脆弱 → 单点故障 → 编译 → 离场 → 终极追问

课尾：

> **如果一万倍机器放大的东西本来就是错的呢？**

### L05｜原力人生

> 胜利 → 不安 → 价值冲突 → 承担 → 同行 → 留下 → 闭环

终局：

> **什么真正值得被复制一万倍？**

---

## 5. Director Layer 统一协议

符号：

```text
[SCREEN] 屏幕主句
[BLACK] 黑屏/留白
[ASK] 只问不答
[WRITE] 学员独写
[CASE] 单任务案例
[HAMMER] 记忆重锤
[TOOL] 工具填写
[CHECK] 闭卷判别
[PAUSE] 停顿
[CLIFF] 课尾悬念
```

统一纪律：

1. 问完关键问题，不立即补答案；
2. 一个案例只服务一个认知动作；
3. 不为了戏剧性新增正典；
4. 不用故事覆盖工具；
5. 每课结尾只回收一个判断 + 一个新问题；
6. Director Layer 不回写冻结 lesson 文件，直到真人证据支持。

---

## 6. 治理状态

```yaml
structure_layer: DESKTOP_VALIDATED_SIMULATED
narrative_layer: CANDIDATE_FOR_LIVE_TRIAL
director_layer: CANDIDATE_FOR_LIVE_TRIAL
narrative_validated_by_round_3: false
director_validated_by_round_3: false
frozen_structure_snapshot_unchanged: true
live_trial: READY_NOT_RUN
real_learner_evidence: false
reusable: false
supersedes_v1: false
```

Director Layer 的加入不改变 Desktop Trial PASS，因为它发生在 Round 3 之后；也不得反过来宣称导演层已经验证。

---

## 7. Live Trial 新增验收维度

除原有理解、判别、工具、负荷、Handoff 外，真人试讲新增：

- Attention Curve：何处注意力明显下降；
- Emotional Turn：哪一次反转真正发生；
- Hammer Recall：24h后能否记住关键重锤；
- Story/Concept Balance：是否只记故事不记判断；
- Cliffhanger Pull：课尾是否自然产生下一课问题；
- Silence Effect：停顿/黑屏是否有效；
- Teacher Rescue：导演动作是否需要额外解释才能成立。

---

## 8. 下一 Gate

> **SMALL_SAMPLE_HUMAN_LIVE_TRIAL_WITH_NARRATIVE_AND_DIRECTOR_LAYER**

建议第一批 3—5 位专家型创业者纵向走完五课，并记录：

- 真人90分钟实际节奏；
- 每段注意力曲线；
- 工具真实完成时间；
- 两个历史 P0 是否复发；
- 四个 Handoff 是否自然；
- 24h 后故事+判断是否仍能重建；
- 30/90天现实实验与 Outcome。

在真人证据前：

```yaml
reusable: false
supersedes_v1: false
```
