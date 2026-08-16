# Trial 09｜L02 V2 vs V3 Directional Desktop A/B

```yaml
trial_id: YL-L02-V3-TRIAL-09
ab_type: directional_desktop_comparison
real_learner_ab: false
run_at: 2026-08-16
v2_baseline: main_L02_PASS_DESKTOP
v3_snapshot: a4015741577e6fbc85001a697cf8d7b2c787b4a4
status: COMPLETE
```

> 这是基于冻结课程结构、既有 V2 Desktop Receipt 与 V3 P01-P06 模拟红队的方向性比较，不是真人随机 A/B。

## 1. 比较矩阵

| 维度 | V2 | V3 | Desktop Verdict |
|---|---|---|---|
| 见名繁守记忆 | 强 | 强 | TIE |
| L01→L02 接口 | 假设更接近“已被选择秘密” | 明确从 Value Candidate 起步 | **V3** |
| 风口化防误解 | 有边界，但 B1 易被务实型学员读成机会识别 | “机会在外面；秘密在判断里” + Why Now Thesis | **V3** |
| 起名化防误解 | 已强调分类/比较 | 三个不等号 + Category Thesis | **V3** |
| 繁的可操作性 | 三链 + 空间复制 | 最小复制单元 + 三链 | **V3** |
| 守的动态性 | 虚实入出 + 时间控制权 | 虚实入出 + Revenue + Asset Delta | **V3** |
| Artifact | 8min、结构轻 | 9-11min、证据/反证 + 30天单关实验 | **V3 actionability / V2 lighter** |
| Cognitive Load | 低到中 | 中，P02/P04 Yellow 无 Red | **V2 slight** |
| 90min 时间 | 纸面 PASS | 纸面 PASS，固定 11min Artifact | TIE_ON_PAPER |
| L03 Handoff | PASS | 6/6 指向“为什么偏偏是我” | **V3 slight** |
| Canon Boundary | PASS | PASS | TIE |
| 现有 Live Readiness | 已 LIVE_TRIAL_READY | 尚待 Human Gate | **V2 current legal status** |

---

# 2. V3 的实质增益

## 2.1 解决新接口漂移

L01 V3.1 的合法离场对象是 `Value Candidate`。

V3 不再把第二课开场偷换为“已被现实证明的秘密”，而是：

```text
Value Candidate
→ 四次现实选择
→ Wealth Candidate
```

这是本轮最重要的工程增益。

## 2.2 四关从并列模型变成连续选择

```text
见｜时代选择
名｜心智选择
繁｜结构选择
守｜时间选择
```

四种财富成为结果，而不是四个并列名词。

## 2.3 B3 找到了更小的行动单位

V2 已有三链；V3 新增“最小复制单元”，让学员必须回答：

> **究竟哪一份价值可以不由本人每次重新制造？**

这对专家型创业者更直接。

## 2.4 B4 与资产复利真正接通

`Revenue + Asset Delta` 让“守”不再只像竞争战略，而与原力母公理一致：

> 每一次结果是否成为下一次更强的输入？

---

# 3. V2 仍然更强的部分

1. 现役版本已经有正式 Desktop Receipt，法权更成熟；
2. Artifact 更轻，课堂风险更低；
3. 理论层更少，讲师执行成本略低。

因此不能因为 V3 结构更完整就宣告现役 V2 失效。

---

# 4. A/B 总裁决

```yaml
winner_interface_rigor: V3
winner_misconception_resistance: V3
winner_actionability: V3
winner_cognitive_lightness: V2
winner_current_legal_live_readiness: V2
v3_red_team: PASS
v3_recall_proxy: PASS_6_OF_6
v3_should_be_abandoned: false
v3_should_replace_v2_now: false
```

课程工程结论：

> # **V3 已经在 Desktop 层证明值得进入 Human Review；但现役 V2 仍是当前唯一已经具备 Live-ready 法权的版本。**

下一步：

> **Human Review → 若批准 V3 Live Trial → 真人计时/四误解/Artifact/真实24h → 再做真实 Promotion Decision。**
