# YEA1｜Yuanli Entrepreneurship Asset Architecture Sync Design
## 原力创业资产生成架构 · GitHub 同步设计

**Date**: 2026-08-23  
**Status**: `WRITTEN_SPEC_HUMAN_ACCEPTED`
**Human design decision**: `ACCEPT_YEA1_ARCHITECTURE_SYNC_DESIGN`  
**Human written-spec decision**: `ACCEPT_YEA1_WRITTEN_SPEC`
**Acceptance receipt**: `project/yea1/YEA1-WRITTEN-SPEC-ACCEPTANCE-v0.1.yaml`
**Implementation plan**: `docs/superpowers/plans/2026-08-23-yea1-entrepreneurship-asset-architecture-sync.md`
**Working repository**: `moonstachain/yuanli-strategy-trilogy`  
**Working branch**: `design/yea1-architecture-sync`  
**Baseline main**: `1553de3d5a8bdceba29ecd89eb4224d4e5626d15`  
**Canon effect of this spec**: `NONE`  

---

## 0｜Purpose

YEA1 does not replace the existing Yuanli Entrepreneurship four canonical actions.

The existing canonical sequence remains:

```text
B1 原力借势
→ B2 品类独创
→ B3 模式升维
→ B4 壁垒锁定
```

YEA1 adds a first-principles structural projection that explains what economic state transition each canonical action performs when Yuanli Entrepreneurship is viewed as an **asset-generation system**.

The new structural projection is:

```text
一大势
→ 两账户
→ 三链路
→ 四壁垒
```

Its economic compression is:

```text
空间
→ 价值
→ 规模
→ 时间
```

Its asset-state transition is:

```text
Opportunity
→ Demand Asset
→ Scalable Cashflow Asset
→ Controlled Compounding Asset
```

Mother sentence:

> **去一个越来越大的世界，做一件越来越值钱的事，造一台越来越会赚钱的机器，建立一个越来越难被取代的系统。**

YEA1 exists to make this logic explicit, machine-readable, governable, testable, and reusable without creating a parallel Canon.

---

# 1｜Authority Constitution

## 1.1 Current repository authority

The current repository constitution states:

```text
yuanli-strategy-soul
= CANON_AUTHORITY

↓ compile / project

yuanli-strategy-trilogy
= PROJECTION / CONTENT ENGINEERING
```

Therefore this repository may design, compile, test, and project YEA1, but it must not independently redefine Soul Canon.

## 1.2 Authority invariants

The following invariants are frozen for YEA1:

```text
B1-B4 canonical names remain unchanged.
YEA1 does not create B5.
YEA1 does not create a fourth Trilogy world.
YEA1 does not create an independent Entrepreneurship Canon.
YEA1 structural language does not silently overwrite historical source language.
YEA1 Human Projection != Canon Authority.
```

## 1.3 Legal status of new language

Before an upstream Soul Human Gate accepts it, the following are:

```yaml
一大势_两账户_三链路_四壁垒: CANDIDATE_STRUCTURAL_PROJECTION
空间_价值_规模_时间: CANDIDATE_ECONOMIC_PROJECTION
增长链_复制链_复利链: CANDIDATE_HUMAN_PROJECTION
asset_state_transition: CANDIDATE_OPERATING_INTERPRETATION
```

No file in Trilogy may claim these are already Soul Canon until an upstream accepted authority receipt exists.

---

# 2｜First-Principles Architecture

YEA1 interprets a business asset as the result of four irreducible economic problems being solved in sequence.

```text
Q1｜Where is value expanding?
Q2｜Why does customer budget flow to us?
Q3｜Can that value be scaled into owner cash flow?
Q4｜Why does that cash flow remain ours through time?
```

The four answers are:

```text
Value Space
→ Value Density
→ Value Scale
→ Value Duration
```

These are not arithmetic scores. They are orthogonal structural dimensions whose absence creates distinct failure modes.

### Failure if Value Space is absent

A company may execute well inside a shrinking or economically trivial value pool.

### Failure if Value Density is absent

A large market may exist, but customer budget does not preferentially flow to the company.

### Failure if Value Scale is absent

Demand exists, but growth requires proportional founder time, labor, capital, or complexity; the business remains a job or project rather than an asset.

### Failure if Value Duration is absent

Cash flow exists, but competition rapidly reallocates the economic surplus.

Therefore the causal progression is:

```text
World
→ Demand
→ Cashflow
→ Control
```

and the asset progression is:

```text
Opportunity State
→ Demand Asset
→ Scalable Cashflow Asset
→ Controlled Compounding Asset
```

---

# 3｜B1 Crosswalk｜原力借势 × 一大势 × Value Space

## 3.1 Canon action

```text
B1 原力借势
```

## 3.2 Structural projection

```text
一大势｜去一个越来越大的世界
```

## 3.3 Economic dimension

```text
Value Space / Runway
```

## 3.4 First-principles question

> **未来十年，新增价值会在哪里大量产生？**

This is not a sector-hotness question. It asks whether technology, demographics, institutions, cost curves, channels, or behavior are producing an expanding value pool.

## 3.5 Founder qualification boundary

YEA1 preserves the existing `势 × 力` logic.

A large world alone does not authorize entrepreneurship. The founder must have a credible asymmetric fit with the opportunity.

```text
Expanding World
× Founder Asymmetry
→ Strategic Field
```

## 3.6 Output

```text
Strategic Field / Opportunity Asset
```

Minimum output fields for future machine representation:

```yaml
world_transition:
value_pool:
why_now:
runway_hypothesis:
founder_asymmetry:
invalidators:
```

## 3.7 Human compression

> **一势给空间。**

---

# 4｜B2 Crosswalk｜品类独创 × 两账户 × Value Density

## 4.1 Canon action

```text
B2 品类独创
```

## 4.2 Structural projection

```text
两账户｜做一件越来越值钱的事
```

## 4.3 Economic dimension

```text
Value Density / Willingness to Pay / Budget Allocation
```

## 4.4 Two strategic value logics

YEA1 introduces two strategic value accounts as an upper-level compression. They do not delete the historical four psychological accounts.

### Functional Account｜功能账户

```text
Existing Job
→ Better Efficiency
→ Extreme Value-for-Money
```

The company wins by making an existing job cheaper, faster, easier, more reliable, or more efficient.

Strategic language:

```text
极致性价比
```

Economic logic:

```text
Cost Logic / Efficiency Delta
```

### Value Account｜价值账户

```text
Old Job Definition
→ Higher-Value Outcome Definition
→ Innovation 10x
```

The company changes what the customer believes is worth paying for.

Strategic language:

```text
创新十倍好
```

Economic logic:

```text
Outcome Logic / Value Definition Delta
```

## 4.5 Relationship with the existing four psychological accounts

The existing psychological-account taxonomy remains a deeper customer-psychology projection:

```text
两大价值账户
│
├── 功能账户
│   └── 功能 / 成本 / 效率
│
└── 价值账户
    ├── 情绪价值
    ├── 社交价值
    └── 投资价值
```

Therefore:

```text
Two strategic value accounts != replacement of four psychological accounts.
```

## 4.6 Output

```text
Demand Asset
```

Minimum output fields:

```yaml
sweet_user:
valuable_job:
value_account: functional | value
budget_source:
category_definition:
mental_position:
willingness_to_pay_logic:
invalidators:
```

## 4.7 Human compression

> **两户给价值。**

---

# 5｜B3 Crosswalk｜模式升维 × 三链路 × Value Scale

## 5.1 Canon action

```text
B3 模式升维
```

## 5.2 Structural projection

Existing operating language in current Entrepreneurship materials remains:

```text
前链路
× 后链路
× 财链路
```

YEA1 adds the human asset-language projection:

```text
增长链
× 复制链
× 复利链
```

## 5.3 Economic dimension

```text
Value Scale / Scalability / Assetization
```

## 5.4 First-principles definition

> **把已经成立的用户价值，通过可复制增长、可复制履约与健康经济结构，转化成不再主要依赖创始人持续出售时间的 Owner Cash Flow Machine。**

B3 therefore is not merely `business model design`.

It is the transition:

```text
Human Labor Income
→ System Cash Flow
→ Business Asset
```

## 5.5 Growth Chain｜增长链

Existing operating source label:

```text
前链路
```

First-principles transformation:

```text
Demand
→ Customer Asset
```

Mother question:

> **怎样让一次性市场需求变成可持续复用的客户资产？**

Typical mechanism path:

```text
Attention
→ Lead
→ Customer
→ Retention
→ Repurchase
→ Referral
→ LTV
```

Desired asset state:

```text
Customer Asset
```

The growth chain is mature when each new customer tends to improve future demand generation rather than requiring the company to restart acquisition from zero.

## 5.6 Replication Chain｜复制链

Existing operating source label:

```text
后链路
```

First-principles transformation:

```text
Founder Capability
→ System Capability
```

Mother question:

> **怎样把“我会”变成“系统会”？**

Typical mechanism path:

```text
Knowledge
→ Process
→ Organization
→ Data
→ AI
→ Partner Network
→ Repeated Outcome
```

Desired asset state:

```text
System Asset / Capability Asset
```

Key direction:

```text
Scale ↑
Founder Dependency ↓
Delivery Reliability maintained or ↑
```

## 5.7 Compounding Chain｜复利链

Existing operating source label:

```text
财链路
```

First-principles transformation:

```text
Operating Profit
→ Reinvestable Capital
```

Mother question:

> **企业创造出来的价值，最终有多少能变成 Owner 可以重新配置的资本？**

Typical mechanism path:

```text
Revenue
→ Gross Profit
→ Operating Profit
→ Free Cash Flow
→ Reinvestable Capital
```

Desired asset state:

```text
Capital Asset
```

The financial chain therefore concerns more than accounting profit. It must eventually expose cash conversion quality and the ability to create freely allocable owner capital.

## 5.8 Three-chain invariant

```text
Demand Scale
→ Operational Scale
→ Capital Scale
```

Human compression:

```text
客户越来越多
→ 企业越来越轻
→ 资本越来越厚
```

## 5.9 B3 output

```text
Scalable Cashflow Machine
```

Minimum machine fields:

```yaml
growth_chain:
  demand_source:
  retention:
  repeat_purchase:
  referral:
  ltv_logic:
replication_chain:
  founder_dependency:
  process_reusability:
  systemization:
  data_ai_leverage:
  delivery_reliability:
compounding_chain:
  revenue_model:
  gross_margin_logic:
  unit_economics:
  cash_conversion:
  reinvestable_capital:
owner_cash_flow_interface:
invalidators:
```

## 5.10 Human compression

> **三链给规模。**

---

# 6｜B4 Crosswalk｜壁垒锁定 × 四壁垒 × Value Duration

## 6.1 Canon action

```text
B4 壁垒锁定
```

## 6.2 Structural projection

```text
四壁垒｜建立一个越来越难被取代的系统
```

The existing governed barrier families used in Entrepreneurship materials remain:

```text
虚
实
入
出
```

No fifth barrier is introduced.

## 6.3 Economic dimension

```text
Value Duration / Value Control / Increasing Returns
```

## 6.4 Control interpretation

### 虚｜Mind Control

Controls how the customer understands and names the category.

```text
brand / category / culture / narrative
```

### 实｜Supply Control

Controls scarce capabilities, cost position, physical assets, process, bottlenecks, or supply architecture.

### 入｜Switching Control

Controls accumulated learning, data, workflow, relationship, ecosystem dependence, and sunk cost.

### 出｜Network / Ecosystem Control

Controls network effects, platform effects, bilateral market structure, and ecosystem flywheels.

## 6.5 Three levels of control maturity

```text
Level 1｜Protection
守住已有利润

Level 2｜Concentration
新增价值越来越多地流向企业

Level 3｜Self-Reinforcement
规模越大，控制点越强
```

The B4 target is not merely defense. Its strongest state is:

```text
Scale ↑
→ Advantage ↑
→ More Scale
```

## 6.6 Output

```text
Controlled Compounding Asset
```

Minimum machine fields:

```yaml
mind_control:
supply_control:
switching_control:
network_control:
strategic_control_points:
control_point_function: concentration | durability | both
substitutability:
self_reinforcement:
invalidators:
```

## 6.7 Human compression

> **四垒给时间。**

---

# 7｜Unified Human Projection

The preferred learner-facing structural projection is:

# **一大势 · 两账户 · 三链路 · 四壁垒**

Expanded:

### 一大势｜选一个越来越大的世界

```text
决定：空间
```

### 两账户｜做一件越来越值钱的事

```text
功能账户 → 极致性价比
价值账户 → 创新十倍好
决定：价值
```

### 三链路｜造一台越来越会赚钱的机器

```text
增长链 → 把需求变成客户资产
复制链 → 把个人能力变成系统资产
复利链 → 把利润变成资本资产
决定：规模
```

### 四壁垒｜建立一个越来越难被取代的系统

```text
虚 → 心智控制
实 → 能力 / 供给控制
入 → 关系 / 切换控制
出 → 网络 / 生态控制
决定：时间
```

Crown expression:

> **一势给空间，两户给价值，三链给规模，四垒给时间。**

Long-form crown expression:

> **去一个越来越大的世界，做一件越来越值钱的事，造一台越来越会赚钱的机器，建立一个越来越难被取代的系统。**

---

# 8｜YEA1 as an Asset-Generation Compiler

YEA1 reframes Yuanli Entrepreneurship as a compiler:

```text
World Potential
→ Customer Budget
→ System Cash Flow
→ Controlled Business Asset
```

or:

```text
势能
→ 价值
→ 现金流
→ 资产
```

Therefore the lawful end state of Yuanli Entrepreneurship under YEA1 is not simply `revenue` or `profit`.

It is:

```text
an operating asset that can increasingly produce owner cash flow
without requiring proportional founder time,
with control mechanisms that protect and reinforce that cash flow through time.
```

This is the legal interface to future YWA0 work.

---

# 9｜YWA0 Boundary

YEA1 belongs to the Entrepreneurship side of the future Yuanli Wealth Architecture.

It stops at:

```text
Controlled Business Asset
→ Owner Free Cash Flow
```

YWA0 begins the next question:

> **下一单位自由现金流应该去哪里？**

Future bridge:

```text
YEA1 / 原力创业
Build Asset
↓
Owner Cash Flow
↓
YWA0 Capital Allocation
↓
原力投研
Own Asset
↓
Capital Snowball
↓
Sovereign Optionality
```

YEA1 must not silently absorb portfolio allocation, valuation, security selection, or investment execution semantics.

---

# 10｜Business-to-Asset Bridge Boundary

A later independent battle may define:

```text
YBA0｜Business-to-Asset Bridge
```

Its intended mapping is:

```text
一大势
→ P / expanding value pool

两账户
→ demand value / willingness to pay / budget allocation

三链路
→ value capture / scalability / C seed

四壁垒
→ Xs / strategic control point / durability / increasing returns
```

But YBA0 is explicitly out of scope for YEA1 implementation.

The investment system must retain its own gates:

```text
E / N / V / Xa / Xp / S
```

Invariant:

```text
Great Business != Great Asset != Great Investment@CurrentPrice
```

---

# 11｜Repository Sync Architecture

## 11.1 Upstream authority target｜`yuanli-strategy-soul`

Role:

```text
CANON_AUTHORITY
```

Future upstream work, once repository access is available and separately authorized, should contain only the minimal semantic authority contract:

```text
B1-B4 remain Canon.
YEA1 structural projection is subordinate to B1-B4.
The economic crosswalk is explicitly typed.
No new B5 or parallel entrepreneurship ontology exists.
```

This current Trilogy spec does not execute that upstream change.

## 11.2 Projection repository｜`yuanli-strategy-trilogy`

Role:

```text
PROJECTION / CONTENT ENGINEERING
```

After written-spec approval and a separate implementation plan, expected implementation targets are:

```text
1. A governed YEA1 mother architecture document.
2. A B1-B4 × 1-2-3-4 × economic-dimension crosswalk.
3. Human Projection updates in appropriate Entrepreneurship outline/content files.
4. Concept metadata projections for B1-B4.
5. Atlas machine-readable crosswalk.
6. Replay / Hard Negative package.
7. Governance state + validator where justified by existing repo patterns.
```

No learner-facing baseline should be overwritten before the applicable Human Gate.

## 11.3 Historical/private working projection｜`yuanli-strategy-trilogy-private`

Role:

```text
HISTORICAL_WORKING_PROJECTION
```

YEA1 must not restore this repository as an SSOT.

No duplicate authoritative YEA1 definition should be maintained here.

## 11.4 Investment repository｜`yuanli-invest`

Role:

```text
CONSUMER OF BUSINESS-QUALITY BRIDGE
```

YEA1 itself is not to be copied wholesale into `yuanli-invest`.

Only a later governed bridge should allow investment research to consume the Entrepreneurship control-point and asset-generation semantics.

---

# 12｜Machine-Readable Crosswalk Contract

The future Atlas projection should make the mapping explicit rather than forcing AI systems to infer it from prose.

Illustrative schema:

```yaml
id: B3
canon_action: 模式升维
structural_projection: 三链路
human_projection:
  - 增长链
  - 复制链
  - 复利链
economic_dimension: value_scale
first_principles_question: >-
  已经成立的用户价值，能否脱离创始人时间，规模化转化为 Owner Cash Flow？
asset_state_transition:
  - demand_to_customer_asset
  - founder_capability_to_system_asset
  - profit_to_reinvestable_capital
output_state: scalable_cashflow_machine
canon_effect: none
```

For B1-B4 the machine must be able to distinguish:

```text
canon_action
structural_projection
human_projection
economic_dimension
asset_state_transition
output_state
```

These fields must not be collapsed into a scalar score.

---

# 13｜Replay & Hard-Negative Design

YEA1 should not be promoted merely because the language is elegant.

The first validation package should test whether the four-step architecture explains materially different business species.

Minimum replay set:

```text
Gold 1｜Amazon
Gold 2｜NVIDIA
Gold 3｜茅台 / another scarcity-brand compounder
Hard Negative｜a company with strong demand or scale but failed value control
```

Each replay must be evaluated ex ante where possible and must ask:

```text
B1｜Was the expanding value space identifiable?
B2｜Was the customer budget logic identifiable?
B3｜Did the three assetization chains actually work?
B4｜Did control strengthen, remain static, or decay?
```

Required hard-negative tests include:

```text
Big trend but weak demand capture.
Strong demand but founder-dependent delivery.
High revenue growth but weak cash conversion.
Strong historical cash flow but collapsing control points.
Large moat but no expanding value pool.
```

Promotion must fail if YEA1 can only explain successful companies after the fact.

---

# 14｜Compatibility Rules

YEA1 must preserve existing language while assigning clear status.

```text
借势 / 独创 / 升维 / 锁定
= canonical action language

一大势 / 两账户 / 三链路 / 四壁垒
= structural human projection candidate

前链 / 后链 / 财链
= existing B3 operating language

增长链 / 复制链 / 复利链
= asset-value human projection of B3

功能 / 情绪 / 社交 / 投资
= existing psychological-account taxonomy

功能账户 / 价值账户
= higher-level strategic value-account compression
```

Forbidden semantic mutations:

```text
两账户 replaces four psychological accounts
三链路 becomes three departments
四壁垒 becomes a generic scoring checklist
一大势 becomes sector-hotness forecasting
增长链 becomes only acquisition funnel
复制链 becomes only SOP documentation
复利链 becomes only accounting profit
```

---

# 15｜Success Criteria

YEA1 implementation is successful only if all of the following hold.

## 15.1 Governance

```yaml
b1_b4_names_unchanged: true
new_parallel_canon: false
b5_created: false
private_repo_ssot_restored: false
yuanli_invest_semantics_redefined: false
```

## 15.2 Human comprehension

A learner should be able to explain the four-stage logic as:

```text
空间 → 价值 → 规模 → 时间
```

and should not confuse:

```text
大势 = 热点
账户 = 客单价
三链 = 三个部门
壁垒 = 静态护城河打分
```

## 15.3 Machine clarity

AI should be able to retrieve, for every B1-B4 object:

```text
what canonical action it belongs to,
what structural projection it carries,
what economic dimension it answers,
what asset-state transition it causes,
and what it does not authorize.
```

## 15.4 Reality validity

Replay must show YEA1 can discriminate at least some matched success/failure cases before any Canon-promotion claim.

---

# 16｜Non-Goals

YEA1 does not:

```text
create an investing model;
create a wealth-allocation engine;
change existing investment P/N/X/E/V/S authority;
replace B1-B4;
replace the four psychological accounts;
replace the 16 strategic control points;
create a fifth barrier;
create a numeric Entrepreneurship score;
automatically rewrite courses or public portals;
authorize publication or merge.
```

---

# 17｜Implementation Battles After Spec Approval

After this written spec receives explicit Human Review approval, implementation planning should decompose work into the following battles.

```text
Battle 0｜Authority & Compatibility Freeze

Battle 1｜YEA1 Mother Architecture Artifact

Battle 2｜B1-B4 Crosswalk + Machine Schema

Battle 3｜Trilogy Projection Integration
- outline
- concepts
- atlas
- human projection

Battle 4｜Replay + Hard Negative Validation

Battle 5｜Human Gate / Promotion Settlement

Battle 6｜YBA0 Bridge Design
(separate authorization; not automatically started)
```

No Battle implementation is authorized by this design spec alone.

---

# 18｜Final Architecture Compression

```text
原力创业 Canon

B1 原力借势
→ B2 品类独创
→ B3 模式升维
→ B4 壁垒锁定

        ↓ Structural Projection

一大势
→ 两账户
→ 三链路
→ 四壁垒

        ↓ Economic Physics

空间
→ 价值
→ 规模
→ 时间

        ↓ Asset State

Opportunity
→ Demand Asset
→ Scalable Cashflow Asset
→ Controlled Compounding Asset

        ↓ Wealth Interface

Owner Free Cash Flow
→ Capital Allocation
```

Crown sentence:

> **一势给空间，两户给价值，三链给规模，四垒给时间。**

Mother sentence:

> **去一个越来越大的世界，做一件越来越值钱的事，造一台越来越会赚钱的机器，建立一个越来越难被取代的系统。**

YEA1 therefore defines Yuanli Entrepreneurship as:

> **一套把个人非对称能力放进扩张中的价值世界，通过需求定义、系统复制和战略控制，编译成可持续 Owner Cash Flow 与可复利经营资产的资产生成系统。**

---

# 19｜Current Legal State

```yaml
architecture_direction: HUMAN_ACCEPTED
written_spec: HUMAN_ACCEPTED
implementation_plan: WRITTEN
implementation_execution: NOT_AUTHORIZED
canon_effect: none
merge_authorized: false
publication_authorized: false
```

Next legal action:

```text
HUMAN_REVIEW_WRITTEN_SPEC
```
