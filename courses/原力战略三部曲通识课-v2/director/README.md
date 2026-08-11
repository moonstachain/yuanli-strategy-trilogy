# 原力战略五课 Director Layer

> 结构负责“讲什么”，Narrative Layer 负责“为什么愿意追下去”，Director Layer 负责“课堂这一分钟具体发生什么”。

```yaml
layer: director
course_id: YL-TRILOGY-GENERAL-v2
status: director_candidate_for_live_trial
source_structure_snapshot: e05450f800b47ff0360c75cb73365e2011d7ee69
narrative_source: narrative/00-五课叙事总纲.md
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

## 二、统一六段叙事协议

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

## 三、统一导演符号

- `[SCREEN]`：屏幕主句；
- `[BLACK]`：黑屏 / 留白；
- `[ASK]`：只问不答；
- `[WRITE]`：学员独立写；
- `[PAIR]`：同伴短交流；
- `[CASE]`：案例；
- `[HAMMER]`：本课重锤；
- `[TOOL]`：工具填写；
- `[CHECK]`：闭卷判别 / 课堂验收；
- `[PAUSE]`：停顿，不继续解释；
- `[CLIFF]`：课尾悬念。

## 四、三条导演纪律

### 1. 不替学员补脑

问完关键问题，至少留 5—15 秒空白；工具卡允许出现 Unknown。

### 2. 案例只服务一个认知动作

一个案例不能同时承担时代、品类、模式、壁垒、母体、OS 六个任务。每个案例只负责把一个反转打穿。

### 3. 课尾不复习知识清单

每课最后只回收：

> 一个判断 + 一个尚未解决的问题。

让问题把学员推向下一课。

## 五、五课导演文件

- `L01-原力战略-导演脚本.md`
- `L02-原力创业-导演脚本.md`
- `L03-原力资产-导演脚本.md`
- `L04-原力OS-导演脚本.md`
- `L05-原力人生-导演脚本.md`

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
```

特别关注：

- 学员是否被故事打动但忘了判断；
- 学员是否只记故事不记工具；
- 黑屏/停顿是否真的提升注意，而不是拖节奏；
- 课尾自然问题是否仍与下一课一致；
- 24h 后记住的是“剧情 + 判断”，还是只剩一句漂亮话。

> **导演层的目标不是让课堂更热闹，而是让关键判断更难被忘记。**
