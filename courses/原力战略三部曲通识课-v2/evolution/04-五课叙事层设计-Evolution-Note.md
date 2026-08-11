# Evolution Note｜五课叙事层设计

```yaml
evolution_id: YL-TRILOGY-GENERAL-v2-EVO-04
course_id: YL-TRILOGY-GENERAL-v2
change_type: narrative_layer_addition
status: candidate_for_live_trial
canon_effect: none
course_structure_effect: none
frozen_lesson_snapshot_modified: false
```

## 1. 背景

Round 3 Desktop Regression 已证明当前五课结构在模拟桌面条件下能够：

- 五课龙骨闭卷重建；
- 四个 Narrative Handoff 4/4；
- 两个历史 P0 不复发；
- 五张工具达到 L3；
- L03/L04 系统性 Red 消失。

因此下一阶段不再继续增加结构概念，而进入一个新的课程工程问题：

> **如何让已经正确的结构，变成学员愿意一路追下去、能够记住并带入行动的故事？**

## 2. 本轮新增

新增独立目录：

```text
narrative/
├── README.md
└── 00-五课叙事总纲.md
```

核心叙事判断：

> **五课不是五个主题，而是五次危机升级；上一课的成功，必须制造下一课更深的危机。**

总叙事母命题：

> **AI正在把“一万倍机器”交给每个人。未来真正稀缺的，不再是复制能力，而是什么值得被复制。**

五课叙事压缩：

```text
AI让平均变便宜
↓
秘密让差异变值钱
↓
母体让差异持续生成
↓
OS让差异穿越本人
↓
人生决定差异最终去哪里
```

## 3. 五幕危机升级

```text
L1｜时代危机
平均正在被重新定价
↓
L2｜财富危机
秘密不自动变成财富
↓
L3｜主体危机
能力只是果实，不是生成源
↓
L4｜组织危机
原力越强，本人越可能成为单点故障
↓
L5｜生命危机
错误方向同样可以被高效复利
```

## 4. 三个叙事符号

仅保留三个，防止叙事层再次概念过载：

1. **一万倍机器**：AI / 商业模式 / 组织 / 系统的放大能力；
2. **一棵树**：母体 → 判断 → 能力 → 产品 → 成果；
3. **离场测试**：如果你不在现场，什么仍会继续？

## 5. 六段叙事协议

每一课建议遵循：

```text
场景
→ 危机
→ 反转
→ 新眼睛
→ 裁决
→ 悬念
```

叙事层目标不是替换五课教学结构，而是让同样的结构产生更强的注意力、意义感和课间牵引。

## 6. 重要治理边界

本轮**没有**修改 Round 3 唯一冻结输入：

`e05450f800b47ff0360c75cb73365e2011d7ee69`

因此：

```yaml
desktop_trial_structure: PASS_SIMULATED
narrative_layer: CANDIDATE_NOT_DESKTOP_VALIDATED
live_trial: READY_NOT_RUN
real_learner_evidence: false
reusable: false
supersedes_v1: false
```

不能把“结构层通过 Desktop Trial”偷换成“叙事层也已验证通过”。

## 7. 下一验证

真人 Live Trial 应新增叙事层观测：

- 前10分钟是否更快形成时代危机；
- 五次危机升级是否保持注意力；
- “一万倍机器”是否被误解成 AI 工具宣传；
- “一棵树”是否进一步降低 Mother=Capability；
- L04叙事是否进一步降低 OS=Tool Stack；
- L05是否避免鸡汤化；
- 四个 Handoff 是否仍自然产生；
- 24h后记住的是因果故事还是仅剩口诀；
- 叙事是否挤压工具时间。

## 8. 当前裁决

> **结构层已经形成龙骨；叙事层现在形成“命运感”。下一步不再继续纸面美化，而应让真人学员验证这条故事是否真的成立。**
