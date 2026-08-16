# Trial 09｜L02 V3 Live Trial Authorization

```yaml
trial_id: YL-L02-V3-TRIAL-09
candidate_id: YL-TRILOGY-GENERAL-v2-L02-V3-CANDIDATE
status: LIVE_TRIAL_READY
authorized_at: 2026-08-16
live_trial: READY_NOT_RUN
real_learner_evidence: false
real_24h_recall: NOT_RUN
validated_live: false
promotion: NOT_AUTHORIZED
canon_effect: none
```

## 1. Frozen Execution Subject

真人试讲必须使用已冻结的 V3 课程对象，不得边讲边修改：

```yaml
snapshot_branch: snapshot/l02-v3-20260816
snapshot_sha: a4015741577e6fbc85001a697cf8d7b2c787b4a4
```

冻结资产：

- `lessons/secret-life/L02-秘密入世-原力创业-v3-candidate.md`
- `director/secret-life/L02-90MIN-DIRECTOR-v3-candidate.md`
- `deck/secret-life/02-原力创业-秘密入世-PPT蓝图-v3.md`
- `exercises/secret-life/L02-我的秘密入世四关卡-v2.md`
- `evidence/L02-秘密入世-Evidence-Packet-v1.md`

若现场必须新增冻结稿之外的大段解释，必须记为 `teacher_rescue_required: true`，不能静默吸收进课程。

## 2. Live Trial 唯一目标

不是证明 V3 “理论更好”，而是验证：

> **目标学员是否能把同一个 Value Candidate 依次通过见、名、繁、守四道现实选择，并形成一个可执行的 30 天验证关。**

## 3. 必测四误解

### M1｜风口化

失败语言：`见 = 找 AI / 银发 / 出海等热门赛道`。

通过语言接近：

> 机会是外部窗口；见要求我对结构变化形成一个可被现实推翻的非平均判断。

### M2｜起名化

失败语言：`名 = 起名字 / slogan / 差异化文案`。

通过语言接近：

> 名改变的是用户用什么分类、比较对象和判断标准理解价值。

### M3｜规模化

失败语言：`繁 = 多卖 / 多招人 / 多渠道 / 多 Agent`。

通过语言接近：

> 先定义最小复制单元：哪一份价值可以不由本人每次重新制造而再次发生。

### M4｜护城河化

失败语言：`守 = 永远抄不了 / 飞轮是第五壁垒`。

通过语言接近：

> 守只看虚实入出控制权是否随每次成功加深。

## 4. 课堂真实验收

```yaml
real_duration_target: 90min
artifact_live_core_target: <=11min
artifact_completion_rate_target: ">=80%"
artifact_L3_rate_target: ">=70%"
critical_misconception_recurrence_target: 0
interface_drift_target: 0
L03_first_handoff_target: ">=70%"
teacher_rescue_target: 0
```

Artifact 必须使用 L01 V3.1 留下的同一个 `Value Candidate`，不得为了填表换一个更漂亮的新点子。

## 5. 24h Recall

真人试讲结束约 24 小时后，不看材料回答：

1. 见为什么不是找风口？
2. 名为什么不是起名字？
3. 你的最小复制单元是什么？
4. 守为什么不是“别人做不了”？
5. 你未来 30 天只验证哪一关？为什么？

真实 24h Recall 必须独立登记；此前 Desktop Recall Proxy 不得代替。

## 6. L03 Handoff

结课第一自然追问应主要指向：

> **为什么同样面对这些变化，偏偏是我更容易形成这个判断？**

如果大量学员仍停留在“再讲讲四关”“我要不要换赛道”，则 L02→L03 Handoff 失败。

## 7. Stop Conditions

任一情况出现，停止宣称 Live Pass：

- 任一关键误解在多数目标学员中复发；
- `Value Candidate` 被系统性误讲成已验证秘密；
- Artifact 无法在课堂完成或普遍低于 L2；
- 需要频繁 Teacher Rescue；
- B4 漂移出 `虚/实/入/出`；
- 真实课堂明显超时且无法通过最小删减修复。

## 8. Live 后法权

真人试讲完成只允许进入：

```text
LIVE_EVIDENCE_AVAILABLE
→ real 24h recall
→ V2/V3 human A-B review
→ Human Promotion Decision
```

真人试讲本身不自动授权 Promotion、合并替换或 Canon Change。