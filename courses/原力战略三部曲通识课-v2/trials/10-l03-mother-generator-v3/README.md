# Trial 10｜L03 V3 原力母体生成函数 Desktop Trial

```yaml
trial_id: YL-L03-V3-TRIAL-10
candidate_id: YL-TRILOGY-GENERAL-v2-L03-V3-CANDIDATE
status: READY_NOT_RUN
evidence_class: simulated_desktop_trial
real_learner_evidence: false
real_24h_recall: NOT_RUN
canon_effect: none
promotion_authority: human
live_trial: NOT_AUTHORIZED
```

## 1. 目的

验证 L03 V3 是否能让目标学员从：

```text
我最强的技能 / 标签 / 人设 / 成功故事
```

迁移到：

```text
三个跨情境同构痕迹
→ 可反驳 Mother Hypothesis
→ 真实取舍
→ 隐性判断外化
→ 新场景预测
```

本 Trial 不验证“原力母体客观存在”，只验证教学是否能形成一个边界清晰、可证伪、可继续现实验证的 `Mother Hypothesis v0.1`。

## 2. 冻结对象

正式运行前冻结 snapshot：

```yaml
snapshot_branch: TBD
snapshot_sha: TBD
```

冻结资产：

- `lessons/secret-life/L03-秘密寻主-原力资产-v3-candidate.md`
- `director/secret-life/L03-90MIN-DIRECTOR-v3-candidate.md`
- `deck/secret-life/03-原力资产-为什么偏偏是你-PPT蓝图-v3.md`
- `exercises/secret-life/L03-我的原力母体假设卡-v2.md`
- `evidence/L03-秘密寻主-Evidence-Packet-v1.md`

运行中不得修改冻结资产。

## 3. Personas

复用现有：

- P01｜方法很多型专家；
- P02｜成熟经营型企业家；
- P03｜专家 IP 型创业者；
- P04｜AI 工具狂热者；
- P05｜高成就效率主义者；
- P06｜跨域小团队创始人。

P06 已在历史 Regression 使用，因此本轮仅作为 `MATCHED_REFERENCE`，不得称为新的独立 blind holdout。

## 4. 六类必攻误解

### M1｜技能化 Skillization

错误：

> 母体 = 我最擅长的技能 / 核心竞争力。

通过：

> 能区分“已长出的能力”与“反复生成能力的结构”，并继续追问 Generator。

### M2｜人格化 Personalityization

错误：

> 母体 = MBTI / 原型 / 天赋标签 / 超级定位。

通过：

> 能说出标签只描述某些倾向，不能代替跨情境生成机制与证据。

### M3｜使命化 Missionization

错误：

> 母体 = 此生唯一使命 / 永远不能改变的真正自我。

通过：

> 主动使用 `Mother Hypothesis v0.1`，承认可修订、缩小、放弃。

### M4｜故事化 Story Bias

错误：

> 只挑成功故事，为漂亮身份叙事作证。

通过：

> 主动提出至少一个强竞争解释和一个反证。

### M5｜玄学化 Mystification

错误：

> 母体 = 爱 / 连接 / 创造 / 成长 / 影响世界等万能词，无法预测行为。

通过：

> 能落到具体 `注意 → 判断 → 转化 → 价值` 结构，并指向可观察场景。

### M6｜内省闭环 Introspection Closure

错误：

> 我觉得很准 / 很感动 = 已验证。

通过：

> 必须产生真实取舍，并提出新场景预测与失败信号。

## 5. P0 Stop Gate

任一不满足，不得进入 Human Review：

```yaml
skillization_critical_recurrence_target: 0
unfalsifiable_mother_hypothesis_target: 0
ultimate_true_self_claim_target: 0
```

## 6. Secondary Gates

```yaml
personalityization_target: 0
missionization_target: 0
story_bias_without_counterevidence_target: 0
mystification_target: 0
introspection_closure_target: 0
upstream_wealth_candidate_drift_target: 0
artifact_L3_target: 6_of_6
artifact_estimated_time_target: <=12min_equivalent
L04_first_handoff_target: >=5_of_6
canon_boundary_breach_target: 0
teacher_rescue_outside_frozen_script_target: 0
```

## 7. Artifact L3

L3 必须同时包含：

- 3 个跨情境同构痕迹；
- 1 条 Mother Hypothesis；
- 1 个强竞争解释；
- 1 个反证；
- 1 个真实机会成本；
- 1 个新场景预测及失败信号。

如果只得到漂亮标签，最高 L1。

## 8. Recall Proxy

本轮可运行 `Context-Isolated Recall Proxy`，但必须明确：

> **它不是实际 24h Recall。**

建议隔离后只问：

1. 为什么能力不是母体？
2. 为什么 MBTI / 原型不能直接等于母体？
3. 什么叫 Mother Hypothesis，而不是终极真我？
4. 为什么必须有竞争解释和反证？
5. 为什么真正的自我认知必须产生取舍？
6. 为什么母体假设还要预测一个新场景？

## 9. L04 Handoff

第一自然下一问应主要指向：

> **如果这些最贵判断仍只存在于我本人，怎么让它离开我还能继续工作？**

不能把悬念打开到 L05，也不能提前教授 C1—C4。

## 10. 状态机

```text
READY_NOT_RUN
→ freeze snapshot
→ P01-P06 six-misconception red team
→ Recall Proxy
→ Result
→ Human Review
→ Live Trial Authorization
```

本文件不授权真人试讲、替换 baseline 或 Promotion。
