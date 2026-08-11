# Evolution Note 03｜五课 Desktop Trial 闭环搭建

## 事件

在五课授课稿、五张主工具与五套 Deck 蓝图完成 `content_draft` 后，课程进入下一验证阶段。

本次没有执行模拟学员，也没有修改课程正文；只建立可重复、可审计、Fail-Closed 的 Desktop Trial 运行闭环。

## 为什么不能直接开始“凭感觉模拟”

若没有冻结输入、Persona、角色分权、统一测量尺和 Receipt，模拟很容易产生以下假阳性：

- Learner 借用项目记忆自动补答案；
- Teacher 临场救场掩盖课程缺陷；
- 每发现一个问题就修改正文，导致不同 Persona 接受不同版本；
- 把“填完工具”误当成“工具可用”；
- 把模拟隔离回忆冒充真实 24h 学员证据；
- 用总体满意度掩盖关键法权误解。

因此先建设 Trial Contract。

## 冻结输入

Round 1 课程内容冻结于：

`6be729bf56759604f2ce2ff19e5163e2206ae2cf`

该 commit 是 Trial 基础设施写入之前的五课完整课程快照。

## 新增闭环

```text
trials/01-five-lesson-desktop-trial/
├── README.md
├── protocol.md
├── personas/ P01—P05
├── sessions/ L01—L05
├── ledgers/ 4类证据账
├── cross-course/ 2类跨课测试
├── patch-candidates.md
└── DESKTOP-TRIAL-RECEIPT.yaml
```

## 三轮治理

### Round 1｜Blind Run

P01/P02/P03 × L01—L05 = 15 个纵向 Session。

中途禁止改课。

### Round 2｜Adversarial Run

P04/P05 + Red Team，只有 Round 1 证据审阅后才能授权。

### Round 3｜Regression Run

P0/P1 修复后必须创建全新 Persona F，不能用已经见过课程的 Persona 自证修复有效。

## 当前状态

```yaml
trial_contract: ready
desktop_trial: ready_not_run
round_1: ready_not_run
round_2: blocked
round_3: blocked
real_learner_evidence: false
live_trial: not_ready
reusable: false
supersedes_v1: false
```

## 法权不变

- Soul 正典不变；
- A→B→C 后台因果不变；
- B4 仍只有虚/实/入/出四壁垒；
- “强”不是 C5；
- 原力人生不是第四部；
- Desktop Trial 不拥有课程升级最终裁决权。

## 下一允许动作

> Run Round 1：P01/P02/P03 连续走完 L01—L05，生成 15 个 Session 原始证据与四本 Ledger。

在 Round 1 完成前，不修改冻结课程正文。
