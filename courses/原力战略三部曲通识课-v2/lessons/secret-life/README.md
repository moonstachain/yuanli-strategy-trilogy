# 《一个秘密的一生》五幕课程实体重构

```yaml
course_id: YL-TRILOGY-GENERAL-v2
reconstruction_id: YL-SECRET-LIFE-LESSONS-v1
layer: lesson_candidate_reconstruction
status: HUMAN_APPROVED_RECONSTRUCTION_IN_PROGRESS
human_decision_date: 2026-08-13
canon_effect: none
promote_to_main_lessons: false
live_trial_required: true
```

> **一个秘密如何诞生、进入世界、找到主人、获得生命、最终获得方向。**

本目录把 `narrative/03-一个秘密的一生-五幕长篇叙事.md` 编译成五份可教学候选正文。

## 1. 为什么建立 candidate layer

现有 `lessons/01—05`、Director Layer、10 个 Anchor Cut 与逐字稿已经拥有历史桌面验证、史料核验和生产记录。新的“秘密的一生”叙事虽然已获 Human Decision，但尚未经过真人 Live Trial。

因此本轮不直接覆盖既有课程资产，而采用：

```text
现有课程正文 / 已验证 Anchor
        ↓ 作为基线与证据资产
secret-life candidate lessons
        ↓
桌面试跑
        ↓
真人试讲
        ↓
Human Gate
        ↓
再决定是否晋升为主 lessons / director
```

治理原则：

> **不以叙事升级破坏既有证据链；不把候选叙事冒充已验证课程。**

## 2. 五幕唯一长线

| 幕 | 课程 | 秘密状态 | 唯一问题 | 出口危机 |
|---|---|---|---|---|
| I | 原力战略 | 秘密诞生 | 一个不同判断凭什么值得继续相信？ | 真相为什么不自动变成财富？ |
| II | 原力创业 | 秘密入世 | 一个真的秘密怎样被世界理解、复制并留下？ | 为什么偏偏是你更容易看见？ |
| III | 原力资产 | 秘密寻主 | 什么持续生成这些秘密？ | 越有原力，事业是否越依赖本人？ |
| IV | 原力 OS | 秘密得生 | 秘密怎样离开主人仍能判断、行动、学习？ | 如果方向错了，一万倍会发生什么？ |
| V | 原力人生 | 秘密定向 | 什么值得用一生持续生成与复制？ | 回到下一轮新的异常与秘密 |

## 3. 秘密状态机

```text
S0 异常
→ S1 秘密种子
→ S2 秘密候选
→ S3 被现实选择的秘密
→ S4 财富化秘密
→ S5 有源之秘
→ S6 可继承之秘
→ S7 有方向之秘
→ S8 递归之秘
→ 新异常……
```

## 4. 每课必须声明 SECRET_THREAD

```yaml
SECRET_THREAD:
  entering_state:
  opening_object:
  central_question:
  mutation:
  evidence_gate:
  personal_verdict:
  exit_state:
  exit_crisis:
```

## 5. 原力叙事四诀

五课全部服从：

> **一事开天，一问到底，一理贯通，一念照我。**

以及九拍：

> **事 → 异 → 难 → 证 → 光 → 深 → 通 → 名 → 我**

纪律：

- 一个旗舰故事优先于多个浅案例；
- 已核验旧 Anchor 优先作为回声案例与第二证据；
- 新增旗舰故事必须单独过 Evidence Gate；
- 概念延迟命名；
- 每课的成功必须制造下一课危机；
- “秘密”是 narrative object，不替代任何 Soul 正典概念。

## 6. 文件

- `L01-秘密诞生-原力战略.md`
- `L02-秘密入世-原力创业.md`
- `L03-秘密寻主-原力资产.md`
- `L04-秘密得生-原力OS.md`
- `L05-秘密定向-原力人生.md`

## 7. 晋升门

候选版本只有同时满足以下条件，才可申请替代主 lessons：

1. 结构桌面试跑通过；
2. 新增 Anchor 的事实层完成 source verification；
3. 目标学员真人试讲完成；
4. 24h 后能复述五幕与核心机制；
5. 五个唯一产物完成质量不低于旧版；
6. `SECRET_THREAD` 在五课之间无断裂；
7. 未造成正典漂移、概念抢法权或认知负荷恶化；
8. Human Gate 明确批准晋升。

> **当前状态：重构开始，不宣称课程已升级成功。**
