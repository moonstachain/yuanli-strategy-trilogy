# 原力战略五课 Director Layer

> 结构负责“讲什么”，Narrative Layer 负责“为什么愿意追下去”，Director Layer 负责“课堂这一分钟具体发生什么”。

```yaml
layer: director
course_id: YL-TRILOGY-GENERAL-v2
status: flagship_anchor_patch_ready_for_live_trial
source_structure_snapshot: e05450f800b47ff0360c75cb73365e2011d7ee69
narrative_sources:
  - narrative/00-五课叙事总纲.md
  - narrative/01-叙事内核-小切口大纵深.md
anchor_evidence_pack: ../evidence/01-五课旗舰小切口证据包.md
anchor_cut_count: 10
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

## 三、当前十个旗舰小切口

| Lesson | Anchor Cut 1 | 只负责 | Anchor Cut 2 | 只负责 |
|---|---|---|---|---|
| L01 原力战略 | **1455 古腾堡圣经** | 复制成本突变 | **1997 Deep Blue** | 旧能力身份边界被机器跨越 |
| L02 原力创业 | **2007 Nokia vs iPhone** | 见：旧世界最强时新生产函数已出现 | **Nintendo Wii** | 名：改变谁算玩家、如何分类价值 |
| L03 原力资产 | **1854 John Snow** | 找/证：异常、反证、行动 | **1971 屠呦呦 Sample 191** | 炼：判断改写方法 |
| L04 原力 OS | **1935 Boeing Model 299** | 单点记忆/状态不可治理 | **Toyota Jidoka / Andon** | 异常→停→处理→Learning→Reuse |
| L05 原力人生 | **1783 Washington 交还军权** | 守：价值作为真实约束 | **2022 Patagonia 所有权重构** | 留：价值方向进入制度 |

十个案例均已建立独立事实边界：

> `../evidence/01-五课旗舰小切口证据包.md`

其中明确区分：

```text
FACT
INTERPRET
FORBIDDEN_CLAIM
```

导演脚本不得脱离证据包自行加戏。

## 四、统一导演符号

- `[SCREEN]`：屏幕主句；
- `[BLACK]`：黑屏 / 留白；
- `[ASK]`：只问不答；
- `[WRITE]`：学员独立写；
- `[PAIR]`：同伴短交流；
- `[CASE]`：普通辅助案例；
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

## 五、七条导演纪律

### 1. 不替学员补脑

问完关键问题，至少留 5—15 秒空白；工具卡允许出现 Unknown。

### 2. 一个 Anchor 只服务一个认知动作

一个案例不能同时承担时代、品类、模式、壁垒、母体、OS 六个任务。

如果同一历史对象必须再次出现，只能作为 `CALLBACK`，不得重新变成第二个概念证明器。

### 3. 概念尽量延迟命名

能让事实、异常和两难先工作，就不要在开头报概念定义。

概念应尽量在 `[CONCEPT_REVEAL]` 处出现，让学员产生：

> “原来这个机制就叫这个名字。”

### 4. 证据强度决定叙事强度

如果证据不足以支持弧光，降低叙事强度，不补人物内心、不补精确数字、不把争议写成确定事实。

### 5. 事后结果不能抹掉当时的不确定性

任何成功案例都必须恢复当时的两难：

> **另一条路为什么在当时也合理？**

如果课堂让学员觉得“这不是显而易见吗”，说明导演失败。

### 6. FACT 与 INTERPRET 必须口头可区分

教师应能随时说清：

> “到这里是史料；从这里开始是原力战略对它的解释。”

特别禁止：

- 给历史人物宣布“原力母体”；
- 把企业结果归因于单一课程机制；
- 用结果反向编造人物动机。

### 7. 课尾不复习知识清单

每课最后只回收：

> 一个判断 + 一个尚未解决的问题。

让问题把学员推向下一课。

## 六、五课导演文件

- `L01-原力战略-导演脚本.md`｜古腾堡 + Deep Blue
- `L02-原力创业-导演脚本.md`｜Nokia/iPhone + Wii
- `L03-原力资产-导演脚本.md`｜John Snow + 屠呦呦
- `L04-原力OS-导演脚本.md`｜Model 299 + Toyota
- `L05-原力人生-导演脚本.md`｜Washington + Patagonia

当前 5 个文件均已完成第一轮旗舰 `ANCHOR_CUT` 九拍 patch。

这意味着“下一轮 director patch 的最小要求”已从待办变成当前基线：

```yaml
anchor_cut_count_per_lesson: 2
required_marks:
  - ANCHOR_CUT
  - ANOMALY
  - DILEMMA
  - EVIDENCE
  - ARC
  - DEEP_DIVE
  - TRANSFER
  - CONCEPT_REVEAL
  - PERSONAL_VERDICT
```

## 七、Live Trial 必须额外观察

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
fact_interpret_separation: not_run
concept_reveal_timing: unknown
mechanism_transfer: not_run
personal_verdict_quality: not_run
cross_discipline_overload: unknown
```

特别关注：

- 学员是否被故事打动但忘了判断；
- 学员是否只记人物不记异常；
- 学员24h后能否用故事还原判断；
- 学员能否在一个没讲过的新场景里迁移判断；
- 学员能否说清“哪句是事实、哪句是课程解释”；
- 黑屏/停顿是否真的提升注意，而不是拖节奏；
- 课尾自然问题是否仍与下一课一致；
- 跨学科是否增加解释力，而不是制造认知负荷。

> **导演层的目标不是让课堂更热闹，而是让关键判断更难被忘记、更容易被迁移，并且不牺牲证据诚实。**
