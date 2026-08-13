# 原力战略五课 Director Layer

> 结构负责“讲什么”，Narrative Layer 负责“为什么愿意追下去”，Director Layer 负责“课堂这一分钟具体发生什么”。

```yaml
layer: director
course_id: YL-TRILOGY-GENERAL-v2
status: director_candidate_for_live_trial
source_structure_snapshot: e05450f800b47ff0360c75cb73365e2011d7ee69
narrative_sources:
  - narrative/00-五课叙事总纲.md
  - narrative/01-叙事内核-小切口大纵深.md
applied_to_frozen_lessons: false
validated_by_round_3: false
live_trial_required: true
canon_effect: none
```

## 一、导演层唯一任务

Director Layer 不重写课程正典，不新增模块，也不改五课已通过 Desktop Regression 的知识结构。

它只控制课堂体验：

- 什么时候进入场景；
- 什么时候制造危机；
- 什么时候停顿；
- 什么时候黑屏；
- 哪一句必须成为重锤；
- 什么时候让学员写；
- 什么时候不解释；
- 什么时候让案例只做一件事；
- 什么时候完成工具；
- 什么时候留下下一课悬念。

## 二、双层叙事协议

### 课程级宏观六段

每一课都遵守：

```text
场景
↓
危机
↓
反转
↓
新眼睛
↓
裁决
↓
悬念
```

最高纪律：

> **上一课的成功，必须制造下一课更深的危机。**

### 旗舰故事级微观九拍

每课选择 1—2 个真正打穿判断的 `ANCHOR_CUT`，优先遵守：

> **事 → 异 → 难 → 证 → 光 → 深 → 通 → 名 → 我**

也就是：

```text
入现场
→ 见异常
→ 设两难
→ 亮硬证据
→ 出高弧光
→ 下机制纵深
→ 跨学科/跨尺度同构
→ 概念升起
→ 回到学员本人
```

微观九拍不是固定九页PPT，而是认知推进顺序。

## 三、统一导演符号

- `[SCREEN]`：屏幕主句；
- `[BLACK]`：黑屏 / 留白；
- `[ASK]`：只问不答；
- `[WRITE]`：学员独立写；
- `[PAIR]`：同伴短交流；
- `[CASE]`：案例；
- `[ANCHOR_CUT]`：本课旗舰小切口；
- `[ANOMALY]`：必须被看见的异常；
- `[DILEMMA]`：站在当时的真实两难；
- `[EVIDENCE]`：硬证据 / 来源支撑；
- `[ARC]`：高弧光显影瞬间；
- `[DEEP_DIVE]`：机制纵深；
- `[TRANSFER]`：跨尺度/跨学科迁移；
- `[CONCEPT_REVEAL]`：概念首次命名点；
- `[PERSONAL_VERDICT]`：回到学员自己的真实裁决；
- `[HAMMER]`：本课重锤；
- `[TOOL]`：工具填写；
- `[CHECK]`：闭卷判别 / 课堂验收；
- `[PAUSE]`：停顿，不继续解释；
- `[CLIFF]`：课尾悬念。

## 四、五条导演纪律

### 1. 不替学员补脑

问完关键问题，至少留 5—15 秒空白；工具卡允许出现 Unknown。

### 2. 案例只服务一个认知动作

一个案例不能同时承担时代、品类、模式、壁垒、母体、OS 六个任务。每个案例只负责把一个反转打穿。

### 3. 概念尽量延迟命名

能让事实、异常和两难先工作，就不要在开头报概念定义。

概念应尽量在 `[CONCEPT_REVEAL]` 处出现，让学员产生：

> “原来这个机制就叫这个名字。”

### 4. 证据强度决定叙事强度

如果证据不足以支持弧光，降低叙事强度，不补人物内心、不补精确数字、不把争议写成确定事实。

### 5. 课尾不复习知识清单

每课最后只回收：

> 一个判断 + 一个尚未解决的问题。

让问题把学员推向下一课。

## 五、五课导演文件

- `L01-原力战略-导演脚本.md`
- `L02-原力创业-导演脚本.md`
- `L03-原力资产-导演脚本.md`
- `L04-原力OS-导演脚本.md`
- `L05-原力人生-导演脚本.md`

下一轮 director patch 的最小要求：

```yaml
anchor_cut_count_per_lesson: 1_to_2
required_marks:
  - SCENE
  - ANOMALY
  - DILEMMA
  - EVIDENCE
  - ARC
  - CONCEPT_REVEAL
  - PERSONAL_VERDICT
```

## 六、Live Trial 必须额外观察

导演层进入真人试讲后，除了原 Desktop Trial 指标，再记录：

```yaml
attention_drop_points: []
spontaneous_questions: []
emotional_turning_points: []
black_screen_effective: unknown
hammer_recall_24h: not_run
cliffhanger_natural_pull: not_run
story_overpowers_concept: unknown
story_underpowers_concept: unknown
anchor_cut_recall_24h: not_run
anomaly_recognition: not_run
dilemma_authenticity: unknown
evidence_trust: unknown
concept_reveal_timing: unknown
mechanism_transfer: not_run
personal_verdict_quality: not_run
cross_discipline_overload: unknown
```

特别关注：

- 学员是否被故事打动但忘了判断；
- 学员是否只记故事不记工具；
- 学员24h后能否用故事还原判断；
- 学员能否在一个没讲过的新场景里迁移判断；
- 黑屏/停顿是否真的提升注意，而不是拖节奏；
- 课尾自然问题是否仍与下一课一致；
- 跨学科是否增加解释力，而不是制造认知负荷。

> **导演层的目标不是让课堂更热闹，而是让关键判断更难被忘记、更容易被迁移。**
