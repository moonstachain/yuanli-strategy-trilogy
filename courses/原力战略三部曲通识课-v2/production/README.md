# 原力战略三部曲通识课｜课程总制作总控 v1

```yaml
course_id: YL-TRILOGY-GENERAL-v2
production_id: YL-TRILOGY-GENERAL-v2-MASTER-PRODUCTION-v1
layer: production_control
status: ACTIVE
human_gate: APPROVED_TO_START_MASTER_PRODUCTION
started_at: 2026-08-14
canon_effect: none
canon_source: moonstachain/yuanli-strategy-soul
structure_authority: ../CORE-STRUCTURE-v1.md
candidate_lessons: ../lessons/secret-life/
live_trial: not_run
promotion_to_main_lessons: false
```

> # **本阶段的任务，不再是继续发明课程，而是把已经冻结的核心结构生产成可讲、可演、可练、可验、可回写的五幕课程作品。**

---

# 1. 制作北极星

课程母问题：

> **AI时代，怎样把一个独特生命，活成一个会复利的事业与人生？**

课程叙事对象：

> **一个秘密的一生。**

五幕：

```text
秘密诞生
→ 秘密入世
→ 秘密寻主
→ 秘密得生
→ 秘密定向
→ 新异常 / 新秘密
```

制作原则：

> **正典负责正确，秘密负责记住；故事负责发生，工具负责留下，试讲负责裁决。**

---

# 2. 总制作的六层对象

每一课都必须同时生产六层，不允许只有“课件”。

```text
01 Canon Alignment
   正典对齐：本课究竟允许讲什么、不能讲什么

02 Evidence Packet
   证据包：旗舰故事与关键事实的来源、争议、禁说项

03 Narrative Lesson
   叙事正文：一个危机、一个故事、一个判断、一个裁决、一个产物、一个悬念

04 Director Edition
   导演版：九拍、时间码、画面、停顿、提问、证据露出、概念揭晓

05 Deck + Artifact
   PPT与学员工具：一页一认知动作，工具可当堂完成并进入下一课

06 Trial + Writeback
   桌面试跑、真人试讲、24h Recall、工具质量、下一课追课欲、回写
```

---

# 3. 总制作阶段门

## G0｜核心结构门

要求：

- `CORE-STRUCTURE-v1.md` 已有人类批准；
- 后台 A→B→C 不漂移；
- 前台 1+3+1 不漂移；
- “秘密”保持 narrative object；
- 五课主产物与五幕状态机已定义。

状态：

```yaml
G0_CORE_STRUCTURE: PASS
```

## G1｜L01 叙事发动机证明门

目标：先把第一幕打穿，不同时铺开五课制作。

必须完成：

1. Dyson Evidence Packet；
2. L01 概念叙事授课卡；
3. 0—15 分钟《一个空袋子》逐字导演稿；
4. 90 分钟 L01 Director Secret-Life Edition；
5. L01 Secret-Life Deck Blueprint；
6. 《我的原力战略起点图 v1》对齐；
7. L01 Desktop Trial。

晋级条件：

```text
Evidence PASS_WITH_BOUNDARIES or PASS
+ Four-Move narrative PASS
+ 90min timing PASS
+ Artifact completion PASS
+ Canon boundary PASS
```

当前：

```yaml
G1_L01_ENGINE: IN_PROGRESS
```

## G2｜L02—L05 批量编译门

前提：G1 PASS。

然后按同一协议生产：

```text
L02 秘密入世
L03 秘密寻主
L04 秘密得生
L05 秘密定向
```

禁止在 G1 未通过时，为追求速度同时重写四课导演稿。

当前：

```yaml
G2_L02_TO_L05: BLOCKED_BY_G1
```

## G3｜五幕连续性门

调用：

`../trials/04-secret-life-reconstruction/README.md`

验证：

- SECRET_THREAD 无断链；
- 上一课成功制造下一课危机；
- 五课没有重新初始化世界；
- 五张工具真正前后读取；
- 课程最后回到新异常，形成递归。

当前：

```yaml
G3_CONTINUITY: READY_NOT_RUN
```

## G4｜真人试讲门

目标学员：专家型创业者 / 通识小白。

至少验证：

- 24h 后能否复述五幕生命史；
- 关键概念是否混淆；
- 每课工具能否按时完成；
- 小切口是否真的抓住人；
- 大纵深是否解释增强而不是知识炫技；
- 高弧光是否产生真实人格裁决；
- 是否产生下一课真实追课欲。

当前：

```yaml
G4_LIVE_TRIAL: NOT_RUN
```

## G5｜主课程晋升门

只有 G0—G4 全部通过 + Human Gate APPROVED，才允许：

- 替换 `lessons/01—05` 主正文；
- 替换主 Director；
- 标记 `reusable: true`；
- 进入正式录制与对外交付生产。

当前：

```yaml
G5_PROMOTION: NOT_AUTHORIZED
```

---

# 4. 五课制作矩阵

| 课 | 五幕 | Candidate Lesson | Evidence | Director | Deck | Artifact | Desktop | Live | Promotion |
|---|---|---|---|---|---|---|---|---|---|
| L01 原力战略 | 秘密诞生 | DONE | IN_PROGRESS | NOT_STARTED | BASELINE_EXISTS / SECRET_LIFE_NOT_STARTED | EXISTS | NOT_RUN | NOT_RUN | NO |
| L02 原力创业 | 秘密入世 | DONE | REUSE_VERIFIED_ANCHORS / PACK_PENDING | NOT_STARTED | BASELINE_EXISTS | EXISTS | NOT_RUN | NOT_RUN | NO |
| L03 原力资产 | 秘密寻主 | DONE | REUSE_VERIFIED_ANCHORS / PACK_PENDING | NOT_STARTED | BASELINE_EXISTS | EXISTS | NOT_RUN | NOT_RUN | NO |
| L04 原力OS | 秘密得生 | DONE | REUSE_VERIFIED_ANCHORS / PACK_PENDING | NOT_STARTED | BASELINE_EXISTS | EXISTS | NOT_RUN | NOT_RUN | NO |
| L05 原力人生 | 秘密定向 | DONE | REUSE_VERIFIED_ANCHORS / PACK_PENDING | NOT_STARTED | BASELINE_EXISTS | EXISTS | NOT_RUN | NOT_RUN | NO |

---

# 5. 每课 Definition of Ready

一节课进入 Director 制作前，必须同时满足：

```text
[ ] 唯一危机冻结
[ ] 唯一新判断冻结
[ ] 旗舰故事冻结
[ ] Evidence Packet 可用
[ ] FACT / INTERPRET / FORBIDDEN_CLAIM 分清
[ ] SECRET_THREAD entering/exit state 明确
[ ] 唯一产物已存在
[ ] 下一危机已冻结
```

缺一项，不进入导演制作。

---

# 6. 每课 Definition of Done

一节课不能因为“讲稿写完”就叫 Done。

```text
[ ] 90min Director Edition 完整
[ ] 旗舰故事无史实越权
[ ] 四诀完整
[ ] 九拍完整但不机械
[ ] 概念延迟命名成立
[ ] PPT 一页一认知动作
[ ] 学员工具当堂完成
[ ] 课程结尾产生下一危机
[ ] Desktop Trial PASS
[ ] 真人 Live Trial PASS
[ ] 24h Recall PASS
[ ] Learning 已回写
```

在真人试讲之前最高状态只能是：

```yaml
production_ready_candidate
```

不能标记 `reusable` 或 `validated_live`。

---

# 7. L01 当前唯一 P0

> # **把“一个空袋子”做成整部五幕作品真正成立的第一场戏。**

生产顺序：

```text
P0-1 Dyson Evidence Packet
↓
P0-2 L01 Concept Narrative Card
↓
P0-3 0—15min Cold Open Director Script
↓
P0-4 90min Director Edition
↓
P0-5 Secret-Life Deck Blueprint
↓
P0-6 Desktop Trial
↓
G1 Human Review
```

其他所有“再加案例、再发明概念、同时做四课逐字稿”的请求，默认让位给此 P0，除非 Human Gate 明确改优先级。

---

# 8. 不做清单

总制作阶段明确不做：

- 不增加第四部或第十三模块；
- 不把“秘密”升级为平行正典；
- 不为了漂亮故事篡改历史；
- 不用更多案例解决主故事不够强的问题；
- 不在 Evidence Gate 前写死人物动机；
- 不把学员感动当作掌握；
- 不把桌面试跑当真人验证；
- 不在 Live Trial 前覆盖旧课程主正文。

---

# 9. 总制作成功的最终判据

这套课程真正完成，不是因为五个 PPT 做完。

而是目标学员能够在五课后完成如下迁移：

```text
我有很多能力
→ 我知道什么持续生成我的不同
→ 我知道这种不同如何接受世界选择
→ 我知道怎样让有效价值被事业继承
→ 我知道什么值得被长期放大
→ 我拥有一份可以继续真实验证与回写的《我的原力战略 1.0》
```

并且 24 小时后仍能自然复述：

> **诞生 → 入世 → 寻主 → 得生 → 定向。**

以及：

> **生成 → 选择 → 保留 → 再生成。**

这才叫“课程完成”。
