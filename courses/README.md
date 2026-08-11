# 原力战略三部曲 · 课程实例总账

本目录只管理“课程实例”，不拥有原力战略正典法权。

法权关系：

```text
moonstachain/yuanli-strategy-soul
  └─ 定义正典、课程生产协议与回写规则

moonstachain/yuanli-strategy-trilogy/courses
  └─ 存放具体课程实例、讲稿、PPT蓝图、练习、试讲与Evolution Note
```

## 课程实例登记

| Course ID | 课程 | Version | 当前状态 | Canon Source | Supersedes |
|---|---|---:|---|---|---|
| YL-GENERAL-3MIN | 三分钟原力通识 | v1 | experiment | yuanli-strategy-soul | — |
| YL-TRILOGY-GENERAL | 原力战略三部曲通识课 | v1 | baseline / live_trial_pending | yuanli-strategy-soul | — |
| YL-TRILOGY-GENERAL | 原力战略三部曲通识课 | v2 | narrative_candidate / five_lessons_content_draft | yuanli-strategy-soul | false |

## 课程治理规则

1. Soul 定法，Trilogy 做课；课程语言不自动升级为正典。
2. 新版本不得静默覆盖旧版本；必须保留 baseline 以供真实教学比较。
3. `content_draft` 不等于 `desktop_trial_pass`；`desktop_trial_pass` 不等于 `live_trial_pass`。
4. 未完成真实试讲、迁移验证与 Human Gate，不得标记 `reusable`，不得宣称 supersede 旧版本。
5. 正典冲突时以 Soul 为准；课程实例必须降级或修正。
6. 所有课程升级最终通过 Evolution Note 回写 Soul，由人工裁决是否进入正典或生产协议。

## 当前重点｜v2

`原力战略三部曲通识课-v2` 当前是对 v1 的叙事与课程结构双重重构挑战者。

### 后台正典不变

```text
A 原力资产 → B 原力创业 → C 原力 OS
```

### 前台课程｜1+3+1

```text
01 原力战略｜世界变了
→ 02 原力创业｜见·名·繁·守
→ 03 原力资产｜找·归·炼·证
→ 04 原力 OS｜懂·记·判·行·强
→ 05 原力人生｜守·生·事·人·留
```

对应：

> **1 个母概念 → 3 次事业跃迁 → 1 次人生升维。**

总叙事：

```text
看懂新世界
→ 创造新财富
→ 找到独特的你
→ 建立会进化的事业
→ 决定什么值得穿越时间
```

超级母句：

> **找到这个世界上只有你才能发现的一个秘密，并把它复制一万倍。**

### 当前完成状态

```yaml
five_lesson_architecture: user_framework_approved
lesson_01_yuanli_strategy: content_draft
lesson_02_yuanli_entrepreneurship: content_draft
lesson_03_yuanli_assets: content_draft
lesson_04_yuanli_os: content_draft
lesson_05_yuanli_life: content_draft
exercises_01_to_05: draft
deck_blueprints_01_to_05: draft
desktop_trial: not_run
live_trial: not_run
transfer_validation: not_run
reusable: false
supersedes_v1: false
```

### 五课毕业工具

```text
《我的原力战略起点图 v1》
+
《我的原力秘密四步卡 v1》
+
《我的原力母体假设卡 v1》
+
《我的原力OS一页架构 v1》
+
《我的原力人生一页纸 v1》
=
《我的原力战略 1.0》候选
```

### 关键边界

- B4只有虚、实、入、出四大壁垒；飞轮不是第五壁垒。
- “强”只是 C1—C4 递归后的结果，不是 C5。
- 原力人生是整合课，不是第四部、不是第十三模块。
- 原120分钟三幕稿继续保留为 `legacy_single_session_candidate`。

### 下一闸门

> **停止继续堆内容，开始五课 desktop trial 与误解审计。**
