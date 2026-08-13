# Evolution Note｜“一个秘密的一生”五幕课程实体重构

```yaml
evolution_id: YL-TRILOGY-GENERAL-v2-EV08
observed_at: 2026-08-13
status: RECONSTRUCTION_COMPLETE_FOR_DESKTOP_TRIAL
canon_effect: none
live_trial: not_run
promotion: not_authorized
```

## 1. Human Decision

用户明确批准：

> **把《原力战略三部曲通识课 v2》按照“一场关于一个秘密如何诞生、进入世界、找到主人、获得生命、最终获得方向”的五幕长篇叙事进行修改和细化，并完整开始执行。**

本轮执行采用：

> **一事开天，一问到底，一理贯通，一念照我。**

## 2. 本轮核心变化

此前五课虽然已有“五次危机升级”，但主要主语仍是“你”：时代逼问你、市场逼问你、自己逼问你、事业逼问你、人生逼问你。

本轮新增统一 Narrative Object：

> **秘密。**

五课重新编译为：

```text
L01 秘密诞生
→ L02 秘密进入世界
→ L03 秘密找到主人
→ L04 秘密获得生命
→ L05 秘密获得方向
→ 回到下一轮新的异常与秘密
```

## 3. 新增课程候选层

新增：

```text
lessons/secret-life/
├── README.md
├── L01-秘密诞生-原力战略.md
├── L02-秘密入世-原力创业.md
├── L03-秘密寻主-原力资产.md
├── L04-秘密得生-原力OS.md
└── L05-秘密定向-原力人生.md
```

没有覆盖原有 `lessons/01—05`。

原因：旧版课程、Director、Anchor 与 evidence 已拥有历史验证资产，而新版长篇叙事尚未经过 Live Trial。

治理裁决：

> **新叙事先进入 candidate layer；验证后再申请晋升，不以创新破坏证据链。**

## 4. 五课 Secret State

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
→ 新异常
```

## 5. 概念法权裁决

继续保持：

```text
canonical_concept:
  原力战略
  原力资产
  原力创业
  原力 OS
  A1-C4

canonical_cross_cutting_concept:
  原力母体

narrative_device / narrative_object:
  秘密
  秘密 × 一万倍

integration_only:
  原力人生
```

冻结原则：

> **正典负责正确，秘密负责记住。**

## 6. 已有 Anchor 的新分工

不废弃 PR #12 / #13 已核验的 10 个 Anchor，而将它们从“每课双旗舰主线”重编译为长篇主线的回声证据：

- L01：Gutenberg / Deep Blue → 复制稀缺性与机器能力的今天镜；
- L02：Nokia / Wii → 见 / 名；
- L03：John Snow / Tu Youyou → 注意异常 / 改变判断；
- L04：Model 299 / Toyota → 复杂度外置 / 异常反馈；
- L05：Washington / Patagonia → 主动停止 / 长期方向制度化。

新原则：

> **一个 Anchor 只承担一个最强认知动作，不与“秘密”的长篇主线竞争。**

## 7. 新增 L01 Flagship

L01 candidate 引入 James Dyson “空袋仍无吸力 → 工业旋风 → 纸板原型 → 原型迭代 → 现实/市场选择”作为“秘密诞生”的旗舰故事。

当前状态严格为：

```yaml
dyson_anchor: CANDIDATE_TO_VERIFY
```

正式真人使用前必须完成独立 Evidence Packet。

特别登记：

- 不把 `5,127` 写成“5126次失败+最后一次成功”；
- 不把行业拒绝单因果写成“袋子利润”；
- 不使用事后成功反推当时确定性；
- 1978/1979 等时间口径若来源冲突，必须显式裁决。

## 8. 新增 Trial Gate

新增：

`trials/04-secret-life-reconstruction/README.md`

验证顺序：

```text
SECRET_THREAD continuity
→ 原力叙事四诀
→ Canon boundary
→ 旧 Anchor 复用
→ Dyson Evidence
→ Desktop timing
→ Human Live Trial
→ 24h recall
→ Tool completion
→ Human Gate
```

## 9. 本轮没有做什么

没有：

- 修改 Soul 正典；
- 修改 A→B→C 因果顺序；
- 把秘密升级成正典概念；
- 把原力人生升级成第四部；
- 覆盖主 lessons；
- 覆盖 Director Scripts；
- 宣称 Dyson 史实已全部核验；
- 宣称真人叙事效果已验证。

## 10. 当前状态

```text
Narrative Master Arc: COMPLETE
Five candidate lessons: COMPLETE
SECRET_THREAD: WIRED_5_OF_5
Old verified anchors: RETAINED_AND_REPURPOSED
Dyson evidence: PENDING_VERIFICATION
Desktop Trial 04: READY_NOT_RUN
Live Trial: NOT_RUN
Promotion to main lessons: NOT_AUTHORIZED
Canon effect: NONE
```

## 11. 下一批最优执行顺序

```text
P0｜Dyson Evidence Packet
↓
P0｜L01 0—15分钟逐字导演稿
↓
P1｜五幕 Secret Thread 桌面连续性试跑
↓
P1｜把 L02—L05 现有 Director Script 做 continuity patch
↓
P1｜PPT 母视觉改成“秘密状态机”
↓
P2｜真人 Live Trial
↓
Human Gate｜决定是否替换主 lessons
```

> **本轮完成的是“长篇叙事进入课程实体”的第一阶段闭环，不是课程升级效果的最终证明。**
