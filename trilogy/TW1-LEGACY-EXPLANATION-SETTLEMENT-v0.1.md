# TW1｜Legacy Explanation Settlement v0.1

> status: `CANDIDATE_PROJECTION_CONVERGENCE`
> upstream authority: `moonstachain/yuanli-strategy-soul@9441586acb638da9819ff13ca03f7ae68a034dc2`
> canon_effect: `none`

## 1. Ruling

TW1 只收敛 **Projection 的解释法权**，不修改 Soul Canon。

当前唯一允许的层级关系是：

```text
Canon
原力资产 × 原力创业 × 原力OS

↓ architecture interpretation

Source × Venture × Evolution

↓ front-stage worldview

源头世界 × 现实世界 × 未来世界

↓ user memory hook

回到源头 → 进入现实 → 创造未来
```

> **正典名负责准确，三个世界负责看懂。**

## 2. Active vs legacy

| 表达 | TW1 裁决 | 还能不能用 | 使用边界 |
|---|---|---|---|
| 原力资产 / 原力创业 / 原力OS | `CANON_NAME` | 是 | 仍是三部正典名称 |
| Source / Venture / Evolution | `ARCHITECTURE_INTERPRETATION` | 是 | 解释生成、选择、保留/进化 |
| 源头世界 / 现实世界 / 未来世界 | `WORLDVIEW_NARRATIVE_DEVICE` | 是 | 前台理解层，不得反向改名 Canon |
| 向内 / 向外 / 向上 | `HISTORICAL_AXIS_DESCRIPTOR` | 限制使用 | 仅作历史教学描述；C 轴前台优先改为“向时间｜未来” |
| 人 / 事 / 法 | `HISTORICAL_TEACHING_DESCRIPTOR` | 限制使用 | 不承担三部本体关系法权 |
| 主根 / 左腿 / 右腿 | `HISTORICAL_NARRATIVE_DEVICE` | 限制使用 | 不再作为当前三部关系主模型 |
| U 型理论 / 跨越鸿沟 / 莫比乌斯 | `EXTERNAL_EXPLANATORY_LENS` | 是 | 只能解释局部，不得定义 A/B/C |
| 「你」× AI | `LEGACY_AMPLIFICATION_METAPHOR` | 限制使用 | AI 只可作为 Amplifier，不得成为三部曲母公理或法权主体 |
| 秘密 × 一万倍 | `NARRATIVE_DEVICE` | 是 | 课程/传播可用，不得升级为 Canon |

## 3. Three Worlds precision

### 源头世界

```text
原力母体
→ A1 发现母体
→ A2 回到母体
→ A3 获得原力
→ A4 显化原力
→ 原力资产
```

因此：

- `源头世界 != 原力资产改名`；
- `原力母体 != Human Design / MBTI / 星盘 / 人格类型`；
- 测评只可作为 Source Lens / Evidence Lens。

### 现实世界

```text
B1 原力借势
→ B2 品类独创
→ B3 模式升维
→ B4 壁垒锁定
```

因此：

- `现实世界 != 赚钱世界`；
- Revenue 只是 Reality Outcome 的一个字段。

### 未来世界

```text
C1 一纸文脉
+ C2 一个大脑
+ C3 一张地图
+ C4 一条链路
```

因此：

- `未来世界 != AI 未来`；
- `未来世界 != 科技趋势`；
- 它回答的是今天的身份、知识、判断、行动、结果与学习如何被未来继承并继续做功。

## 4. Recursive relation

```text
源头世界_n
→ 现实世界_n
→ 未来世界_n
→ Learning / Reuse
→ 源头世界_n+1
```

压缩为：

> **生成 → 选择 → 继承 → 再生成。**

## 5. Projection source rule

TW1 后，Trilogy 世界观投影的唯一机器源是：

```text
trilogy/_atlas/worldview-v1.json
```

README、`portal-map.json`、三世界总图以及后续 Atlas/总纲入口，都只能编译这个 source，不得各自重新发明三部关系。

## 6. Generated legacy pages

当前仓库中部分历史生成页与深层 outline 仍保存旧表达，例如：

- `trilogy/_atlas/trilogy-master-outline.json`
- `trilogy/原力战略三部曲-总纲.html`
- `trilogy/原力三部曲-文脉骨架座舱.html`

TW1 对它们的治理裁决是：

```text
DEEP_CONTENT / HISTORICAL_PROJECTION
!= CURRENT_WORLDVIEW_AUTHORITY
```

它们可以继续作为章节素材、历史解释与深层目录，但关于“三本究竟是什么关系”的当前解释，一律服从 `worldview-v1.json`。

后续若要重构其渲染器，必须保持“判断/渲染分离”，不得把旧生成页重新升格为判断源。

## 7. Course isolation

TW1 不修改：

```text
courses/
trials/
director/
deck/
exercises/
lessons/
```

PR #18 / #20 等真人课程与 Shadow 轨道保持独立。

TW2 只有在 TW1 合并后，且有新的人类授权时才可进入课程 Overlay。
