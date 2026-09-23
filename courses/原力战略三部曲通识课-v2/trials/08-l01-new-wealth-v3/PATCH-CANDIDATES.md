# Trial 08｜Patch Candidates

```yaml
trial_id: YL-L01-V3-TRIAL-08
status: CANDIDATES_ONLY
applied: false
human_gate_required: true
evidence_class: simulated_desktop_trial
```

> 按 Desktop Trial Protocol，本轮只记录 `Misconception → Evidence → Root Cause → Minimal Patch → Regression Test`。本文件不授权修改冻结课程。

---

# P0-01｜秘密 ≠ 商业机会

```yaml
severity: P0
trigger: P02 critical semantic drift
```

## Misconception

> “秘密就是抓住一个别人没抓住的 AI 商业机会。”

## Evidence

- Round 1 P02 即时重建：“我 = 找一个真正能赚钱、别人没抓住的机会”。
- Recall Proxy P02 再次把完整公式回忆成“好机会 × AI 放大 × 资产”。

## Root Cause

V3 已经排除了内幕、信息差、点子，但仍把“变化的时代 × 用户贵问题”讲得很像机会识别；对务实型企业家，“独特生成源”没有形成足够锋利的区分。

## Minimal Patch

在秘密定义后增加一组 20—30 秒对照，不新增概念：

```text
机会：外部窗口，很多人都可能同时看见。
秘密：你对这个窗口形成的非平均判断，必须回答：
为什么你更容易持续看见？
你看见的到底是哪一个贵问题？
现实准备怎么推翻你？
```

皇冠边界：

> **机会在外面；秘密是你对机会形成、并愿意交给现实验证的非平均判断。**

## Regression Test

P02 必须在 context-isolated recall 中主动区分“机会”和“秘密”，且 Value Candidate 不得只写赛道/风口。

---

# P1-01｜Artifact 无课内执行时间槽

```yaml
severity: P1_BLOCKER
trigger: P01-P05 estimated completion 15-19min; director slot 0min
```

## Evidence

当前 Director 0—90 分钟全部已有讲授动作；Artifact 只在文末声明“课内完成率 ≥80%”，没有实际时间槽。

既有 Protocol 要求 L01 Desktop Time Budget `≤13min`。

## Root Cause

V3 把理论升级当成了“加法”，但没有把学员产物重新纳入 90 分钟资源约束。

## Minimal Patch

把完整清算表拆成：

### Live Core｜课堂 10—12min

只填：

```text
A 1项：正在变便宜的能力
B 1项：AI越强越需要训练的非平均价值
C 1项：即使短期回报下降仍值得继续验证的问题
D 1项：要把哪次输出变成下一次输入
E 1句：Value Candidate
```

### 24h Extension｜课后

再补 A/B 各 3 项、证据场景、停止项与完整资产化清单。

时间从以下位置回收：

- 古腾堡 + Deep Blue 合计压 2min；
- 三本书名不单独讲作者背景，回收 2min；
- 稀缺阶梯不逐项解释，回收 2min；
- AI 杠杆链压 2min；
- 三部曲地图压 1min；
- 其他停顿与重复解释回收 2—3min。

## Regression Test

P01-P06 Live Core `estimated_completion_time ≤12min` 且质量 ≥L3。

---

# P1-02｜三本书 + 稀缺阶梯造成高负荷峰值

```yaml
severity: P1
trigger: P02 HIGH, P04 HIGH, P05 MEDIUM_HIGH
```

## Root Cause

三本书名、三条定律、11级稀缺阶梯、价值主权、秘密公式在 20—59 分钟密集出现。V3 的理论正确，但工作记忆主线可能被“知识点”挤掉。

## Minimal Patch

前台只要求记四个字：

> **能 → 贵 → 值 → 我**

三本书降级为“脚注式理论桥”，不进入闭卷强制记忆。

稀缺阶梯从 11 项降成三个代表性迁移：

```text
答案多 → 好问题贵
方案多 → 判断贵
选择多 → 品味/价值取舍贵
```

其他项保留到讲师备注 / Evidence Packet，不在主屏逐项点亮。

## Regression Test

P02/P04 active novel concepts peak 不得达到 Red；结课必须先复述因果链，而非书名/阶梯。

---

# P1-03｜L02 Handoff 被 L03/L05 竞争

```yaml
severity: P1
trigger: P03 competing L03 pull; P05 competing L05 pull
```

## Root Cause

V3 同时打开三个高张力未闭合问题：

1. 为什么偏偏是你更容易看见？（L03）
2. 什么真正值得做？（L05气质）
3. 秘密凭什么被世界理解、付钱？（L02）

虽然最后一页指向 L02，但 P03/P05 会被更贴近自身偏好的问题抢走。

## Minimal Patch

- L03 不再用开放问句形成悬念，只标注：“来源问题后面再处理，本课先不证明。”
- “值”在本课必须收束为 **Value Candidate 可修订**，不展开人生终局。
- 89—90 分钟只保留唯一未闭合问题：

> **一个值得的秘密，为什么还赚不到钱？**

## Regression Test

P01-P06 至少 5/6 的第一自发下一问必须指向 L02：市场理解、付费、品类、复制或壁垒。

---

# P1-04｜Value Candidate 被使命化

```yaml
severity: P1
trigger: P05 soft missionization
```

## Minimal Patch

在 Artifact C/E 之间增加一句边界：

> **Value Candidate 是下一阶段值得验证的方向，不是“唯一使命”；它可以被现实修订、缩小、放弃或重写。**

C 区问题从：

> “如果不再必须靠它谋生，你仍愿意长期为什么投入生命？”

课堂 Live Core 版改成：

> **“即使短期回报下降，你仍愿意继续验证哪个人群/问题至少一年？为什么？”**

完整 Deep Utopia 追问可保留在课后 Extension 或 L05。

## Regression Test

P05 不得把 Value Candidate 回忆为“终极使命 / 一生唯一目标”。

---

# P2-01｜理论桥的法权提示可更轻

当前对三本书边界已经正确，但课堂反复说“不是预测/不是正典”可能破坏流动。

Minimal Patch：讲师口头只保留最必要一句；完整法权边界放 Speaker Notes / Evidence Packet。

---

# Patch Queue 总结

```yaml
P0: 1
P1: 3
P1_blocker: 1
P2: 1
current_course_change_authorized: false
next_gate: HUMAN_PATCH_GATE
```

推荐最小执行包：`P0-01 + P1-01 + P1-02 + P1-03 + P1-04`。

目标不是削弱 V3 理论，而是：

> **保留“能→贵→值→我”的发动机，同时恢复 V2 的低负荷、工具时隙和单一悬念纪律。**
