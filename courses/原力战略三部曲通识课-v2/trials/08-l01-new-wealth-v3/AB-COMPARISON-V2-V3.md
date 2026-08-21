# Trial 08｜L01 V2 vs V3 Desktop A/B

```yaml
comparison_id: YL-L01-V2-V3-AB-20260816
evidence_class: simulated_desktop_trial
real_learner_evidence: false
randomized_live_ab: false
comparison_type: evidence_weighted_directional
v2_source: trials/05-l01-secret-life-desktop/RESULT-v2.md
v3_source:
  - ROUND-1-PERSONA-SESSIONS.md
  - ROUND-2-RED-TEAM.md
  - CONTEXT-ISOLATED-RECALL-PROXY.md
```

> 本文件是 Desktop A/B，不冒充真人随机对照。V2 与 V3 的试验年代、问题集与 Persona 暴露并不完全相同，因此只有“方向性比较”法权。

---

# 1. 两版最小差异

## V2｜秘密诞生 / Dyson Engine

核心结构：

```text
一个空袋子
→ 不同判断
→ 现实选择
→ 保留
→ 再生成
→ 原力战略
→ 秘密 × 一万倍
```

优势：一个故事、一条机制、延迟命名、强人格裁决。

## V3｜AI时代的新财富算法

核心结构：

```text
能：能力丰裕
→ 贵：稀缺迁移
→ 值：目的显现/价值主权
→ 我：值得被放大的秘密
→ AI 杠杆
→ 时间保留
```

优势：直接解释 AI 时代为什么必须重新计算财富，并把“秘密 × 一万倍”推导出来。

---

# 2. 用户指定五项核心指标

## A｜“能贵值我”即时重建

V2：不存在该显式四字结构，无法同指标直接评分。

V3：

```yaml
full_reconstruction: 4/5 in P01-P05
partial: 1/5
matched_P06: PASS
```

Verdict：`V3_WIN_ON_EXPLICIT_SPINE`

说明：V3 的“能→贵→值”非常稳；“我”会被 Persona 吸回机会/定位/使命，是唯一薄弱点。

---

## B｜Recall / 24h

V2 已有 Desktop 结论：24h 强制记忆被压缩为五项，但真实 24h `NOT_RUN`；V2 Desktop 只证明认知负荷与纸面闭卷设计通过。

V3：Context-Isolated Recall Proxy 为 5/6 可接受、1/6 critical semantic drift；真实 24h 同样 `NOT_RUN`。

Verdict：`NO_REAL_24H_WINNER`

方向性判断：

- V2 更容易记住**故事物件与机制**；
- V3 更容易记住**AI时代因果链与皇冠句**；
- V3 的“我 / Value Candidate”延迟迁移仍不稳。

---

## C｜秘密误解率

V2 历史 Red Team 必攻：秘密 = 商业机会；最终 V2 Round 3 historical P0 recurrence = 0，但该结论来自 patched five-course regression persona，不是本次同一问题集 A/B。

V3 本轮：

```yaml
critical_recurrence: 1/6
soft_confusion: 2/6
main_failure_mode:
  - 商业机会化
  - 定位化
  - 使命化（Value Candidate）
```

Verdict：`V2_CURRENT_BASELINE_WIN`

进入 Live Gate 的最低门槛要求 Critical Misconception recurrence = 0，因此 V3 当前不满足。

---

## D｜价值清算表完成率

V2：现役 L01 明确在 72—82 分钟给 Artifact 10min；Desktop v2 结论为 `PASS_ON_PAPER`，仍待真人实测。

V3：90min Director 把 0—90 全部用于讲授/悬念，Artifact 只在文末声明目标，没有独立执行时间槽。

P01-P05 估时：

```text
P01 18min
P02 17min
P03 15min
P04 16min
P05 19min
```

全部超过既有 L01 Desktop Budget `≤13min`。

Verdict：`V2_CLEAR_WIN / V3_P1_BLOCKER`

这是当前最明确、无需真人数据即可确认的结构缺陷。

---

## E｜L02 追课欲

V2：现役结课悬念单一——“一个真的秘密为什么还赚不到钱？”；Desktop Result 标记 narrative handoff 可进入第二幕。

V3：

```yaml
clean_L02_pull: P01, P04
L02_with_friction: P02
competing_L03_pull: P03
competing_L05_pull: P05
matched_P06: L02_PASS
```

方向性估计：V3 的“世界凭什么理解、记住、付钱”很强，但课中同时种下 L03（为什么偏偏是你）与 L05（什么值得做）的高张力问题，导致主悬念竞争。

Verdict：`V2_WIN_ON_HANDOFF_PURITY / V3_WIN_ON_TOTAL_CURIOSITY`

课程工程需要的是前者。

---

# 3. 其他关键维度

| 维度 | V2 | V3 | Desktop 判断 |
|---|---|---|---|
| AI时代现实相关性 | 中：AI 90秒 Today Mirror | 高：AI是全课时代背景 | V3 |
| 一个故事的抓取力 | 高：Dyson 单主角 | 中：古腾堡+Deep Blue+三本书 | V2 |
| 理论解释力 | 中高：生成→选择→保留→再生成 | 高：丰裕→稀缺→目的→主体 | V3 |
| 价值主权 | 隐含 | 显式核心 | V3 |
| Cognitive Load | Desktop PASS | P02/P04 出现 HIGH | V2 |
| Delayed Naming | 强 | 较弱：多个理论词提前出现 | V2 |
| Canon Boundary | PASS | PASS | TIE |
| Secret Boundary | 历史 patched PASS | 当前 1 critical + 2 soft | V2 |
| Artifact 可执行性 | 10min slot / PASS_ON_PAPER | 无 slot / 15—19min | V2 |
| L02 Handoff | 单一 | 被 L03/L05 竞争 | V2 |
| 新财富算法解释力 | 中 | 强 | V3 |

---

# 4. A/B 总裁决

## V3 不是“整体输给 V2”

V3 已经证明了三个不可退回的升级：

1. **AI 首先改变能力价格**比“AI 会不会替代人”更高阶；
2. **稀缺迁移 + 价值主权**让“秘密 × 一万倍”不再像口号，而有完整时代因果；
3. **新财富 = 值得的秘密 × 杠杆 × 时间保留**把方向、规模、复利三者第一次统一。

## 但 V3 当前也没有资格替换 V2

原因不是理论错误，而是课程工程失败：

```text
理论深度 ↑
但
Artifact Time Slot = 0
Critical Secret Drift > 0
L02 Handoff Purity ↓
Cognitive Load ↑
```

因此：

```yaml
winner_on_theory_engine: V3
winner_on_current_live_readiness: V2
v3_promotion: NOT_AUTHORIZED
v3_live_trial: NOT_READY_YET
recommended_action: PATCH_THEN_REGRESSION
```

最小目标不是把 V3 改回 V2，而是：

> **保留 V3 的“能→贵→值→我”理论发动机，恢复 V2 的单主线、低负荷、工具时间与单一悬念纪律。**
