# YFA-GC2.1-LT1-SIM｜企业家学员模拟 Live Trial

> 说明：本轮是 **simulated live-trial rehearsal**，不是 Human Live Evidence。用于在真实招募前，用企业家型 Persona 对 90 分钟 L03 v2.2-DT1 做一次“接近课堂”的行为回归。

```yaml
trial_id: YFA-GC2.1-LT1-SIM
lesson: L03 原力资产｜为什么偏偏是你？
input_version: v2.2-DT1
artifact: 我的原力资产生成树 v1.1｜课堂六格主卡
evidence_class: simulated_live_trial_rehearsal
real_human_participants: 0
status: COMPLETE
canon_effect: none
reusable: false
```

# 一、测试目标

本轮不问“内容是否有道理”，只测 7 个教学行为：

1. **30min Artifact Gate**：六格主卡能否在约 30 分钟主动学习时间内形成可检查候选；
2. **Mother≠Capability Gate**：学员是否把职位 / 核心能力 / 行业技能直接写成 Mother；
3. **Self-Endorsement Gate**：是否出现带真实机会成本的“继续认领 / 不再成为”；
4. **Force Bet Gate**：是否能把 Mother 压成一个现实问题上的“原力下注”；
5. **Fruit≠Seed Gate**：是否理解一次成功 / 一次付费仍不等于资产；
6. **Distinct Task2 Gate**：Task2 是否与 Task1 materially distinct；
7. **24h Recall + Transfer Proxy**：离开上下文后能否重建生命树并迁移到陌生场景。

模拟判分：

```text
0 = 未形成 / 严重误解
1 = 在同伴检查后可修正
2 = 无需教师救援即可形成
```

关键规则：

> **如果一个核心误解只能靠教师直接给答案才能修正，本 Persona 该 Gate 记 0，不得因为“老师解释后懂了”算 PASS。**

---

# 二、五类企业家 Persona

## P01｜成熟经营型企业家

```yaml
age_band: 40-50
business: 传统制造/消费企业
experience: 15+年经营
strength: 经营判断、供应链、组织
risk: 把Mother写成“经营能力/战略能力”
```

### 初始六格

**根｜Mother Hypothesis（初稿）**

> 我的母体是“经营判断力强，能看利润和效率”。

**同伴检查**：这句话可直接写进 CEO 核心能力清单 → 退回。

**二稿**

> 我似乎会持续进入“资源很多但真正约束不清”的局面，先找最限制结果的瓶颈，再围绕瓶颈重新排资源优先级；这个模式过去出现在供应链、渠道、现金流和组织调整四类不同任务里。

**反证**

> 在新消费品牌审美/内容判断上，我曾把“效率瓶颈”误当核心问题，结果越优化越偏。

**归**

> 我愿意继续认领“把复杂经营问题压到真正约束”；即使赚钱，也不愿长期做纯人情维系、靠老板本人不断救火的生意。

**原力下注**

> 面对增长停滞问题，我要验证“先找约束再配资源”的生成方式，是否能比全面加码更快找到有效增长杠杆。

**炼**

> 当多个指标同时变差时，优先找最可能支配其他指标的约束，而不是平均救火。

**果实**

> 90天选择一个新业务单元，观察决策周期、库存周转与现金占用是否改善；失败信号：只改善局部指标而系统利润未改善。

**种子 / Task2**

> Task1 留下“约束诊断清单+失败案例”；Task2 用于一个不同区域的新渠道进入决策，而不是同一业务复盘。

### 结果

```yaml
active_work_estimate: 27min
mother_not_capability: 1
self_endorsement: 2
force_bet: 2
fruit_seed: 2
distinct_task2: 2
24h_recall_proxy: 2
transfer_proxy: 2
```

**观察**：成熟经营者最容易在第一版把 Mother 压成“战略/经营能力”；但 `JD 判别 + 三表型` 足以使其自修正，不需要教师给答案。

---

## P02｜专家 IP 型创业者

```yaml
age_band: 35-45
business: 咨询/教育/内容IP
experience: 10+年专业服务
strength: 内容、表达、框架
risk: Mother=内容创作/结构化表达；资产=课程/知识库
```

### 初始六格

**根（初稿）**

> 我的 Mother 是“结构化表达”。

同伴检查：明显是能力标签 → 退回。

**二稿**

> 我反复会在“别人知道很多但不知道该怎么做”的场景里，把分散知识压缩成一条可行动路径；它曾分别长成咨询框架、课程设计、销售诊断和 AI 知识库。

**反证**

> 在需要纯审美创造的品牌项目里，我的“压缩成路径”反而可能把开放探索过早收束。

**归**

> 我愿意继续认领“把复杂知识变成可共同使用的行动秩序”；即使收入高，也不愿长期做追热点、只为了流量而持续生产自己不认同内容的账号。

**原力下注**

> 面对企业家学习后无法行动的问题，我要验证“复杂知识→关键判断→行动路径”的生成方式，是否能提高7天内真实行动率。

**炼**

> 当学员说“信息太多不知道从哪开始”时，优先删除非决定性知识，只保留一个判断与一个下一步动作。

**果实**

> 90天在一门新课中观察：7天行动率、作业完成率、是否能独立迁移；失败信号：满意度高但行动无变化。

**种子 / Task2（初稿）**

> 把课程录下来，下一次继续用。

同伴检查：`Learning Document ≠ Reuse`，且 Task2 不够不同 → 退回。

**二稿**

> Task1 留下“决策压缩规则+错误样例”；Task2 在一个客户战略工作坊中预加载这些规则，看是否减少诊断时间并提高关键问题识别率。

### 结果

```yaml
active_work_estimate: 31min
mother_not_capability: 1
self_endorsement: 2
force_bet: 2
fruit_seed: 1
distinct_task2: 1
24h_recall_proxy: 2
transfer_proxy: 2
```

**观察**：专家 IP 最危险的不是 Mother，而是 **“我有课程/知识库，所以我有资产”**。`果实≠种子` 能触发修正，但 Task2 设计仍接近上限，需要互评时间。

---

## P03｜AI 原生创业者

```yaml
age_band: 28-38
business: AI SaaS / Agent / 自动化
experience: 5-10年
strength: 工具、产品、自动化
risk: 把AI能力当本人Force；把自动化当资产化完成
```

### 初始六格

**根（初稿）**

> 我的 Mother 是“AI 自动化和快速学习新工具”。

同伴检查：如果明天工具全部换代，这句话是否还能解释你？回答“不一定” → 退回。

**二稿**

> 我反复对“人还在重复做、但规则其实已经足够清晰”的工作产生强烈不适，会先找可形式化的决策边界，再把重复劳动交给系统；过去长成脚本、产品流程、销售自动化与 Agent 设计。

**反证**

> 在高信任、高模糊的人才判断中，我曾过度形式化，损害了关系质量。

**归**

> 我愿意继续认领“把可形式化的重复工作编译成系统”；即使增长快，也不愿长期靠制造 AI 焦虑卖没有真实 Outcome 的工具。

**原力下注**

> 面对销售跟进遗漏，我要验证“先定义人类判断边界、再自动化”的方式，是否比直接上 Agent 更少漏掉高价值客户。

**炼**

> 当一个任务准备自动化时，先写出“必须由人判断的边界”和失败升级条件，再让 AI 执行其余部分。

**果实**

> 90天观察漏跟率、人工升级率和成交质量；失败信号：效率提高但高价值客户损失增加。

**种子（初稿）**

> Prompt 和 Agent 工作流就是资产。

同伴追问：“下一任务是否因为过去学习而改变判断？”

**二稿**

> Task1 保存“哪些情况禁止自动化”的负样本规则；Task2 用在客服投诉分类，与销售跟进任务不同，检查边界规则是否能减少错误自动处理。

### 结果

```yaml
active_work_estimate: 29min
mother_not_capability: 1
self_endorsement: 2
force_bet: 2
fruit_seed: 1
distinct_task2: 2
24h_recall_proxy: 2
transfer_proxy: 2
```

**观察**：`AI-assisted performance ≠ Human Force` 必须保留；对 AI 创业者而言，“种子”如果只写 Prompt/Agent，会出现假资产。当前同伴追问可以修正，但属于 Live Trial 必测红线。

---

## P04｜高成就效率主义型创始人

```yaml
age_band: 35-45
business: 连续创业/高速增长公司
strength: 执行、目标、速度
risk: 把长期成就驱动误当Mother；机会成本写成抽象情绪
```

### 初始六格

**根（初稿）**

> 我就是目标感强、执行力强，任何事都想做到第一。

同伴检查：这是能力/驱动描述，而且无法区分真实方向与补偿性驱动。

**二稿仍卡住**

> 我持续寻找最快达成目标的方法。

此时仅靠“JD判别”仍无法进入真正生成机制；需要额外问题：

> **如果没有排名、没有掌声、没有人知道，你还会对哪类问题持续投入？**

在该提示后形成：

> 我真正反复投入的不是“赢”，而是把看似不可能的复杂目标拆成一组可以被组织持续推进的关键约束与节奏。

**归（初稿）**

> 我不愿再焦虑内耗。

不通过：没有机会成本。

在现有提示“必须是角色/项目/工作方式”下二稿：

> 即使赚钱，我也不愿继续做必须靠我24小时高压盯人才能增长的业务。

**原力下注**

> 面对跨部门高难项目，我要验证“约束拆解+节奏治理”能否让项目在不依赖创始人持续催促下按里程碑推进。

其余四格均可形成。

### 结果

```yaml
active_work_estimate: 34min
mother_not_capability: 0
self_endorsement: 1
force_bet: 2
fruit_seed: 2
distinct_task2: 2
24h_recall_proxy: 2
transfer_proxy: 2
teacher_rescue_needed_for_mother: true
```

**观察｜P0候选**：对高成就/强补偿型企业家，现有 `三表型 + JD判别` 仍可能不足以穿透“赢/执行/目标感”。需要一个非常短的 **External Reward Ablation Question**：

> **如果没有排名、掌声、身份和外部认可，你还会持续对什么问题投入？**

这不是新增一套理论，而是 A2 Self-Endorsement 的最小消融题。

---

## P05｜家族责任 / 关系驱动型企业家

```yaml
age_band: 40-55
business: 家族企业/二代转型
strength: 责任、关系、长期主义
risk: 把“责任感/照顾家人”直接写成Mother或使命
```

### 初始六格

**根（初稿）**

> 我的 Mother 是“责任感，对家人和员工负责”。

同伴检查：价值词，不是生成机制。

**二稿**

> 我反复会注意“一个系统里谁承担了别人看不见的代价”，并试图重新设计规则，让责任、权利和收益更匹配；过去出现在家族分工、员工激励、供应商合作和客户售后。

**反证**

> 有时我把所有人的代价都纳入自己责任，导致决策过慢、边界不清。

**归**

> 我愿意继续认领“让关系里的责任与收益更公平可持续”；即使短期利润更高，也不愿长期靠压供应商账期和员工隐性加班获取利润。

**原力下注**

> 面对家族企业新一代激励，我要验证“先识别隐性代价与责任错配”的方式，是否能降低关键人才流失并提高责任清晰度。

**炼 / 果实 / 种子**

均可形成，Task2 选择供应商合作协议重构，与家族人才激励 materially distinct。

### 结果

```yaml
active_work_estimate: 30min
mother_not_capability: 1
self_endorsement: 2
force_bet: 2
fruit_seed: 2
distinct_task2: 2
24h_recall_proxy: 2
transfer_proxy: 2
```

**观察**：“责任感”与“使命”非常容易被误当 Mother，但 `价值词≠生成机制` 的一句教师提示即可避免，不需要再加入 Complex 术语。

---

# 三、横向结果

## 3.1 六格完成时间（模拟估计）

```text
P01 27min
P02 31min
P03 29min
P04 34min
P05 30min
median = 30min
range = 27-34min
```

裁决：

> **课堂 36 分钟主动工作预算基本合理，但高成就型 Persona 存在超时风险。**

## 3.2 核心 Gate

| Gate | 无教师救援直接通过 | 同伴/现有规则后通过 | 仍需教师救援 |
|---|---:|---:|---:|
| Mother ≠ Capability | 0/5 | 4/5 | **1/5** |
| Self-Endorsement / 真实机会成本 | 4/5 | 1/5 | 0/5 |
| 原力下注可形成 | 5/5 | 0/5 | 0/5 |
| 果实 ≠ 种子 | 3/5 | 2/5 | 0/5 |
| Task2 materially distinct | 3/5 | 2/5 | 0/5 |
| 24h主脊柱回忆代理 | 5/5 | 0/5 | 0/5 |
| 陌生场景迁移代理 | 5/5 | 0/5 | 0/5 |

### 关键判断

`Mother ≠ Capability` 仍然是整个 L03 最大真人风险，而且风险已经从“普通能力标签”转移到更难的：

> **成就驱动 / 赢 / 责任 / 自我要求等高身份认同词。**

---

# 四、24h Recall Proxy

不给术语表，只问：

> “昨天那棵树，从下到上是什么？”

五类 Persona 均能恢复到近似：

```text
我怎样形成 / 我选择继续认领什么
→ 根：为什么总长出相似差异
→ 主干：选一件现实问题下注
→ 炼成可重复判断
→ 果实：真实世界结果
→ 种子：留下并进入下一个不同任务
```

这说明：

> **生命树比 `Mother / Force Thesis / Validated Force / Atomic Force Asset` 术语链更适合 24h 记忆。**

因此前台继续坚持“根 / 主干 / 炼 / 果实 / 种子”，后台保留正式对象，是正确的。

---

# 五、陌生场景迁移测试

题目：

> “如果你最强的某项能力明天被 AI 商品化，你怎么判断自己有没有失去原力？”

五类 Persona 均能迁移到：

1. 能力只是当前载体；
2. 回看根是否还能长出别的载体；
3. 选择一个新现实问题做原力下注；
4. 需要重新训练、验证；
5. AI 输出变好本身不等于人的 Force 已增强。

裁决：`PASS_SIMULATED`。

---

# 六、LT1-SIM 暴露出的唯一 P0 候选

## P0-SIM-01｜External Reward Ablation 缺失

高成就型企业家可能把：

```text
赢
第一
成就
高标准
执行
```

写成最深层的 Mother，并且 `JD判别` 无法充分反驳，因为这些词未必是岗位能力。

建议在 A1→A2 之间新增 **一题，不新增一页理论**：

> # **如果没有排名、掌声、身份和外部认可，你还会持续对什么问题投入？**

作用：

- 不是证明“真实自我”；
- 不是否定外部驱动；
- 只是对 Mother 候选做一次 external-reward ablation；
- 如果答案完全消失，就把 Mother 置信度降级，并带入 A2 Self-Endorsement 继续判断。

这是本轮唯一建议在真人 LT1 前应用的 P0 patch。

---

# 七、两个 P1 Watch，不建议继续加课

## W1｜专家 IP：资产=内容仓库

真实 Live Trial 必须观察：

> 学员是否把“课程/文档/Prompt/知识库已保存”当成 Asset。

判别必须坚持：

> **Learning Document ≠ Reuse**。

## W2｜AI 创业者：工具资产=Force Asset

真实 Live Trial 必须观察：

> 学员是否认为 Agent / Workflow 能跑，就证明本人 Force/Force Asset 成立。

必须坚持：

> **AI-assisted Performance ≠ Human Capability Growth**。

---

# 八、模拟裁决

```yaml
result: CONDITIONAL_PASS_FOR_REAL_LT1
simulated_personas: 5
structural_blockers: 0
p0_candidate_before_real_live_trial: 1
p1_watch_items: 2
median_active_work_estimate: 30min
24h_recall_proxy: PASS_5_OF_5
transfer_proxy: PASS_5_OF_5
mother_capability_without_teacher_rescue: 4_of_5
fruit_seed_after_peer_check: 5_of_5
distinct_task2_after_peer_check: 5_of_5
```

本轮只能说明：

> **v2.2-DT1 已经足够成熟，可以在应用一个极小 P0 patch 后进入真实小样本 Live Trial。**

它不能说明：

- 真人 90 分钟真实可完成；
- 真实 24h 记忆成立；
- 真实企业家愿意写出机会成本；
- 真实 7d 行为迁移；
- 90d Task2 Reuse 已发生。

---

# 九、下一 Gate

建议顺序：

```text
LT1-SIM
↓
应用 P0-SIM-01 External Reward Ablation Question
↓
LT1-HUMAN｜3-5名真实企业家
↓
课堂结束即时检查
↓
24h Blind Recall
↓
7d Transfer Check
↓
90d Task2 Reuse（另属现实长期 Gate）
```

真实 LT1 前禁止继续增加新理论、新案例或新工具。
