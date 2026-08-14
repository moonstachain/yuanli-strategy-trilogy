# 原力战略三部曲通识课｜课程总制作总控 v1

```yaml
course_id: YL-TRILOGY-GENERAL-v2
production_id: YL-TRILOGY-GENERAL-v2-MASTER-PRODUCTION-v1
layer: production_control
status: ACTIVE
human_gate: APPROVED_TO_START_MASTER_PRODUCTION
started_at: 2026-08-14
last_updated_at: 2026-08-14
canon_effect: none
canon_source: moonstachain/yuanli-strategy-soul
structure_authority: ../CORE-STRUCTURE-v1.md
candidate_lessons: ../lessons/secret-life/
live_trial: not_run
promotion_to_main_lessons: false
```

> # **本阶段的任务，不再是继续发明课程，而是把已经冻结的核心结构生产成可讲、可演、可练、可验、可回写的五幕课程作品。**

制作原则：

> **正典负责正确，秘密负责记住；故事负责发生，工具负责留下，试讲负责裁决。**

---

# 1. 总制作六层

每一课必须同时生产：

```text
01 Canon Alignment
02 Evidence Packet
03 Narrative Lesson
04 Director Edition
05 Deck + Artifact
06 Trial + Writeback
```

不能因为“讲稿写完 / PPT 做完”就叫完成。

---

# 2. 总制作阶段门

## G0｜核心结构门

```yaml
G0_CORE_STRUCTURE: PASS
```

依据：

- `../CORE-STRUCTURE-v1.md`
- 五幕 `SECRET_THREAD`
- 前台 1+3+1 / 后台 A→B→C

---

## G1｜L01 叙事发动机证明门

当前已经完成：

```text
[PASS_WITH_BOUNDARIES] Dyson Evidence Packet
[PASS] L01 Concept Narrative Card
[PASS] 0—15 Cold Open
[PASS] 15—37 Reality Trial
[PASS] 37—90 Reveal & Verdict
[PASS] L01 90min Director consolidated entry
[PASS] Secret-Life Deck Blueprint
[PASS_ON_PAPER] Secret-Life Artifact
[PASS] Desktop Trial v2
```

状态：

```yaml
G1_L01_ENGINE: PASS_DESKTOP
L01: LIVE_TRIAL_READY
L01_LIVE_TRIAL: READY_NOT_RUN
```

重要边界：

> `LIVE_TRIAL_READY` 只表示具备真人试讲资格，不表示真人效果已验证，不允许替换主课。

---

## G2｜L02—L05 批量编译门

前提 G1 已满足，因此正式解锁：

```yaml
G2_L02_TO_L05: READY_TO_START
```

生产顺序冻结为：

```text
L02 秘密入世｜原力创业
↓
L03 秘密寻主｜原力资产
↓
L04 秘密得生｜原力OS
↓
L05 秘密定向｜原力人生
```

每课复制的不是 L01 内容，而是 L01 已证明的生产协议：

```text
Evidence
→ Concept Narrative Card
→ Director
→ Deck + Artifact
→ Desktop Trial
```

---

## G3｜五幕连续性门

调用：

`../trials/04-secret-life-reconstruction/README.md`

当前：

```yaml
G3_CONTINUITY: READY_NOT_RUN
```

只有 L02—L05 都达到 Desktop PASS 后执行。

---

## G4｜真人试讲门

当前：

```yaml
G4_LIVE_TRIAL: NOT_RUN
```

L01 已可先做单课 Live Trial；五幕整体验证必须等待五课生产完成。

Live 必测：

- 真实时间；
- 24h Recall；
- 概念不混淆；
- Artifact 完成率；
- 高弧光是否真实成立；
- 下一课追课欲。

---

## G5｜主课程晋升门

```yaml
G5_PROMOTION: NOT_AUTHORIZED
```

只有：

```text
G0 PASS
+ G1—G3 PASS
+ G4 Live PASS
+ Human Gate APPROVED
```

才允许替换现有主 lessons / Director，或标记 `reusable: true`。

---

# 3. 五课制作矩阵｜Current

| 课 | 五幕 | Candidate Lesson | Evidence | Director | Deck | Artifact | Desktop | Live | Promotion |
|---|---|---|---|---|---|---|---|---|---|
| **L01 原力战略** | 秘密诞生 | DONE | **PASS_WITH_BOUNDARIES** | **90MIN READY** | **SECRET-LIFE READY** | **PATCHED READY** | **PASS v2** | READY_NOT_RUN | NO |
| L02 原力创业 | 秘密入世 | DONE | REUSE_VERIFIED_ANCHORS / PACK_PENDING | NOT_STARTED | BASELINE_EXISTS | EXISTS | NOT_RUN | NOT_RUN | NO |
| L03 原力资产 | 秘密寻主 | DONE | REUSE_VERIFIED_ANCHORS / PACK_PENDING | NOT_STARTED | BASELINE_EXISTS | EXISTS | NOT_RUN | NOT_RUN | NO |
| L04 原力OS | 秘密得生 | DONE | REUSE_VERIFIED_ANCHORS / PACK_PENDING | NOT_STARTED | BASELINE_EXISTS | EXISTS | NOT_RUN | NOT_RUN | NO |
| L05 原力人生 | 秘密定向 | DONE | REUSE_VERIFIED_ANCHORS / PACK_PENDING | NOT_STARTED | BASELINE_EXISTS | EXISTS | NOT_RUN | NOT_RUN | NO |

---

# 4. L01 已形成的生产资产

## Evidence

- `../evidence/L01-Dyson-Evidence-Packet-v1.md`

## Director

- `../director/secret-life/L01-CONCEPT-NARRATIVE-CARD-v1.md`
- `../director/secret-life/L01-00-15-COLD-OPEN-v1.md`
- `../director/secret-life/L01-15-38-REALITY-TRIAL-v1.md`
- `../director/secret-life/L01-38-90-REVEAL-AND-VERDICT-v1.md`
- `../director/secret-life/L01-DESKTOP-PATCHSET-v1.md`
- `../director/secret-life/L01-90MIN-DIRECTOR-v1.md`

## Deck

- `../deck/secret-life/01-原力战略-秘密诞生-PPT蓝图-v1.md`

## Artifact

- `../exercises/secret-life/L01-我的原力战略起点图-v1.md`

## Trial

- `../trials/05-l01-secret-life-desktop/RESULT-v1.md`
- `../trials/05-l01-secret-life-desktop/RESULT-v2.md`

---

# 5. L01 证明出来的“课程生产协议”

以后四课不复制故事，而复制这条生产链：

```text
唯一危机
↓
旗舰小切口
↓
独立 Evidence Packet
↓
一问到底
↓
现实审判 / 高弧光
↓
一理贯通
↓
延迟命名
↓
一念照我
↓
唯一 Artifact
↓
下一幕危机
↓
Desktop Trial
↓
Live Trial
↓
Learning 回写
```

这就是课程总制作的标准发动机。

---

# 6. 每课 Definition of Ready

进入 Director 前必须满足：

```text
[ ] 唯一危机冻结
[ ] 唯一新判断冻结
[ ] 旗舰故事冻结
[ ] Evidence Packet 可用
[ ] FACT / INTERPRET / FORBIDDEN_CLAIM 分清
[ ] SECRET_THREAD entering/exit state 明确
[ ] 唯一产物存在
[ ] 下一危机冻结
```

---

# 7. 每课 Definition of Done

```text
[ ] 90min Director Edition 完整
[ ] 旗舰故事无史实越权
[ ] 四诀完整
[ ] 九拍完整但不机械
[ ] 概念延迟命名成立
[ ] PPT 一页一认知动作
[ ] 学员工具当堂可完成
[ ] 课程结尾产生下一危机
[ ] Desktop Trial PASS
[ ] 真人 Live Trial PASS
[ ] 24h Recall PASS
[ ] Learning 已回写
```

真人试讲之前最高状态：

```yaml
LIVE_TRIAL_READY
```

不得提前标 `reusable` / `validated_live`。

---

# 8. 当前 P0

L01 桌面发动机已经证明。

新的课程制作 P0：

> # **L02《秘密入世｜原力创业》进入完整生产协议。**

目标：

> 不把“见名繁守”讲成四个模型，而是让一个已经真实存在的秘密，亲历“被看见→被理解→被复制→被守住”的四次财富变形。

L02 必须先完成：

```text
P0-1 旗舰故事裁决
P0-2 Evidence Packet
P0-3 Concept Narrative Card
P0-4 90min Director
P0-5 Secret-Life Deck + Artifact
P0-6 Desktop Trial
```

---

# 9. 不做清单

- 不增加第四部或第十三模块；
- 不把“秘密”升级为平行正典；
- 不为漂亮故事篡改史料；
- 不用更多案例掩盖主故事不成立；
- 不把学员感动当掌握；
- 不把 Desktop PASS 当 Live PASS；
- 不在真人验证前覆盖旧课程主正文。

---

# 10. 总制作最终完成判据

五课结束后，目标学员能够完成：

```text
我有很多能力
→ 我知道什么持续生成我的不同
→ 我知道这种不同如何接受世界选择
→ 我知道怎样让有效价值被事业继承
→ 我知道什么值得被长期放大
→ 我拥有一份可继续验证与回写的《我的原力战略 1.0》
```

24h 后仍能自然复述：

> **诞生 → 入世 → 寻主 → 得生 → 定向。**

以及：

> **生成 → 选择 → 保留 → 再生成。**

这才叫课程完成。
