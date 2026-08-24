# YEA1 Entrepreneurship Asset Architecture Sync Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the accepted YEA1 first-principles Entrepreneurship Asset Architecture as a governed, additive, machine-readable Trilogy projection without changing B1–B4 Canon names, promoting a parallel Canon, rewriting learner-facing course baselines, or touching `yuanli-invest` semantics.

**Architecture:** Keep `B1 原力借势 → B2 品类独创 → B3 模式升维 → B4 壁垒锁定` as the canonical action spine. Add a subordinate YEA1 projection layer (`一大势 → 两账户 → 三链路 → 四壁垒`) plus economic dimensions (`空间 → 价值 → 规模 → 时间`) and asset-state transitions. Store the candidate projection once in a dedicated JSON contract, project it into the Entrepreneurship outline and `atlas-v2-chuangye.json`, validate the crosswalk fail-closed, then run four evidence-backed replays before any promotion claim.

**Tech Stack:** Markdown, JSON, YAML, Python 3.12 standard library (`json`, `pathlib`, `unittest`), GitHub Actions, existing Trilogy Atlas and projection patterns.

**Spec:** `docs/superpowers/specs/2026-08-23-yea1-entrepreneurship-asset-architecture-sync-design.md`

## Global Constraints

- `yuanli-strategy-soul = CANON_AUTHORITY`; this repository remains `PROJECTION / CONTENT ENGINEERING`.
- Preserve the exact canonical sequence: `B1 原力借势 → B2 品类独创 → B3 模式升维 → B4 壁垒锁定`.
- Do not create B5, a fourth Trilogy world, or a parallel Entrepreneurship Canon.
- `一大势 / 两账户 / 三链路 / 四壁垒` remain `CANDIDATE_STRUCTURAL_PROJECTION` until a later upstream Soul Human Gate.
- `空间 / 价值 / 规模 / 时间` remain `CANDIDATE_ECONOMIC_PROJECTION` until a later upstream Soul Human Gate.
- `增长链 / 复制链 / 复利链` are a human asset-language projection of B3; preserve `前链路 / 后链路 / 财链路` as existing operating language.
- `功能账户 / 价值账户` must not replace the existing `功能 / 情绪 / 社交 / 投资` psychological-account taxonomy.
- Preserve `虚 / 实 / 入 / 出`; do not create a fifth barrier or reduce B4 to a scalar moat score.
- Do not add numeric YEA1, Entrepreneurship, or right-tail composite scores.
- Do not rewrite current learner-facing course lessons, decks, director scripts, exercises, or live-trial baselines in this battle.
- Do not modify `yuanli-invest`; YBA0 remains a separately authorized future battle.
- Do not claim replay success without source-backed evidence; if evidence cannot be obtained, record `EVIDENCE_BLOCKED` rather than infer facts.
- No merge, publication, course promotion, Soul Canon change, or YBA0 start is authorized by this plan.

---

## File Structure

The implementation is intentionally additive and follows existing TW1 governance patterns.

**Create**

- `project/yea1/YEA1-STATE-v0.1.yaml` — lifecycle state, boundaries, exact-head verification status, next legal action.
- `project/yea1/YEA1-HUMAN-REVIEW-CARD-v0.1.md` — final review questions and promotion boundary.
- `trilogy/YEA1-原力创业资产生成母架构-v0.1.md` — human-readable mother architecture.
- `trilogy/_atlas/yea1-entrepreneurship-asset-architecture-v0.1.json` — single machine-readable candidate projection contract.
- `scripts/yea1/validate_yea1_projection.py` — fail-closed projection validator.
- `scripts/yea1/test_validate_yea1_projection.py` — standard-library unit tests for validator logic.
- `.github/workflows/yea1-architecture-sync.yml` — exact-scope CI gate.
- `trilogy/replays/yea1/README.md` — replay protocol and evidence rules.
- `trilogy/replays/yea1/amazon-pit-replay.md` — Gold replay.
- `trilogy/replays/yea1/nvidia-pit-replay.md` — Gold replay.
- `trilogy/replays/yea1/maotai-pit-replay.md` — Gold replay.
- `trilogy/replays/yea1/webvan-hard-negative.md` — hard negative.

**Modify**

- `trilogy/_atlas/atlas-v2-chuangye.json` — additive YEA1 fields for B1–B4; existing stage text and keyword bodies remain intact.
- `trilogy/原力创业-四级目录.md` — add one clearly labeled candidate projection preface and one compact B1–B4 crosswalk; do not rewrite existing 51-section body.
- `docs/superpowers/specs/2026-08-23-yea1-entrepreneurship-asset-architecture-sync-design.md` — transition written-spec state to Human Accepted and point to acceptance receipt and plan.

**Existing governance input**

- `project/yea1/YEA1-WRITTEN-SPEC-ACCEPTANCE-v0.1.yaml`
- `README.md`
- `project/tw1/TW1-STATE-v0.1.yaml`
- `.github/workflows/tw1-projection-convergence.yml`

---

### Task 1: Freeze YEA1 Governance State and Accepted Spec

**Files:**
- Create: `project/yea1/YEA1-STATE-v0.1.yaml`
- Modify: `docs/superpowers/specs/2026-08-23-yea1-entrepreneurship-asset-architecture-sync-design.md`
- Verify: `project/yea1/YEA1-WRITTEN-SPEC-ACCEPTANCE-v0.1.yaml`

**Interfaces:**
- Consumes: acceptance decision `ACCEPT_YEA1_WRITTEN_SPEC`, accepted spec commit `00ba2e8020ff9d4804ef1a37cb0dafc0fbbd7e9b`.
- Produces: a machine-readable lifecycle state consumed by the validator and Human Review card.

- [ ] **Step 1: Read the authority baseline and acceptance receipt**

Run:

```bash
cat README.md
cat project/yea1/YEA1-WRITTEN-SPEC-ACCEPTANCE-v0.1.yaml
```

Expected authority statements:

```text
yuanli-strategy-soul = CANON_AUTHORITY
yuanli-strategy-trilogy = PROJECTION / CONTENT ENGINEERING
ACCEPT_YEA1_WRITTEN_SPEC
implementation_plan: true
implementation_execution: false
merge: false
```

- [ ] **Step 2: Create the initial YEA1 lifecycle state**

Create `project/yea1/YEA1-STATE-v0.1.yaml` with exactly this state model:

```yaml
schema: yuanli.yea1.state.v0.1
program: YEA1
status: WRITTEN_SPEC_ACCEPTED_IMPLEMENTATION_PLANNED
branch: design/yea1-architecture-sync
baseline_main: 1553de3d5a8bdceba29ecd89eb4224d4e5626d15
written_spec: docs/superpowers/specs/2026-08-23-yea1-entrepreneurship-asset-architecture-sync-design.md
written_spec_acceptance: project/yea1/YEA1-WRITTEN-SPEC-ACCEPTANCE-v0.1.yaml
human_decision: ACCEPT_YEA1_WRITTEN_SPEC

scope:
  mother_architecture: NOT_STARTED
  machine_contract: NOT_STARTED
  atlas_projection: NOT_STARTED
  outline_projection: NOT_STARTED
  validator: NOT_STARTED
  validator_tests: NOT_STARTED
  ci_gate: NOT_STARTED
  replay_amazon: NOT_STARTED
  replay_nvidia: NOT_STARTED
  replay_maotai: NOT_STARTED
  replay_webvan: NOT_STARTED
  human_review_card: NOT_STARTED

protected_boundaries:
  b1_b4_names_changed: false
  b5_created: false
  parallel_canon_created: false
  soul_canon_changed: false
  course_baseline_changed: false
  private_repo_ssot_restored: false
  yuanli_invest_changed: false
  yba0_started: false

promotion:
  candidate_projection_only: true
  soul_promotion_authorized: false
  course_promotion_authorized: false
  publication_authorized: false
  merge_authorized: false

next_legal_action: EXECUTE_YEA1_IMPLEMENTATION_PLAN_AFTER_EXPLICIT_EXECUTION_CHOICE
```

- [ ] **Step 3: Update the spec status without changing its accepted semantics**

Change only the governance header and final legal-state block in the accepted spec:

```text
Status: WRITTEN_SPEC_HUMAN_ACCEPTED
Human written-spec decision: ACCEPT_YEA1_WRITTEN_SPEC
Acceptance receipt: project/yea1/YEA1-WRITTEN-SPEC-ACCEPTANCE-v0.1.yaml
Implementation plan: docs/superpowers/plans/2026-08-23-yea1-entrepreneurship-asset-architecture-sync.md
```

The final legal state must say:

```yaml
architecture_direction: HUMAN_ACCEPTED
written_spec: HUMAN_ACCEPTED
implementation_plan: WRITTEN
implementation_execution: NOT_AUTHORIZED
canon_effect: none
merge_authorized: false
publication_authorized: false
```

- [ ] **Step 4: Verify no unintended content drift**

Run:

```bash
git diff --check
git diff -- docs/superpowers/specs/2026-08-23-yea1-entrepreneurship-asset-architecture-sync-design.md project/yea1/YEA1-STATE-v0.1.yaml
```

Expected: only governance-state changes; no B1–B4 semantic rewrite.

- [ ] **Step 5: Commit**

```bash
git add docs/superpowers/specs/2026-08-23-yea1-entrepreneurship-asset-architecture-sync-design.md project/yea1/YEA1-STATE-v0.1.yaml project/yea1/YEA1-WRITTEN-SPEC-ACCEPTANCE-v0.1.yaml
git commit -m "governance: freeze YEA1 accepted spec state"
```

---

### Task 2: Create the Single YEA1 Machine Contract and Mother Architecture

**Files:**
- Create: `trilogy/_atlas/yea1-entrepreneurship-asset-architecture-v0.1.json`
- Create: `trilogy/YEA1-原力创业资产生成母架构-v0.1.md`
- Modify: `project/yea1/YEA1-STATE-v0.1.yaml`

**Interfaces:**
- Consumes: accepted YEA1 spec definitions.
- Produces: one JSON source for all projection fields plus one human-readable architecture artifact. Task 3 and the validator must consume the exact IDs and field names defined here.

- [ ] **Step 1: Create the machine contract with exact top-level identity**

Create `trilogy/_atlas/yea1-entrepreneurship-asset-architecture-v0.1.json` using this top-level shape:

```json
{
  "schema": "yuanli.entrepreneurship_asset_architecture.v0.1",
  "program": "YEA1",
  "status": "CANDIDATE_STRUCTURAL_PROJECTION",
  "canon_effect": "none",
  "canon_actions_preserved": ["B1 原力借势", "B2 品类独创", "B3 模式升维", "B4 壁垒锁定"],
  "structural_projection": ["一大势", "两账户", "三链路", "四壁垒"],
  "economic_dimensions": ["value_space", "value_density", "value_scale", "value_duration"],
  "human_dimensions": ["空间", "价值", "规模", "时间"],
  "asset_state_chain": ["opportunity", "demand_asset", "scalable_cashflow_asset", "controlled_compounding_asset"],
  "mother_sentence": "去一个越来越大的世界，做一件越来越值钱的事，造一台越来越会赚钱的机器，建立一个越来越难被取代的系统。",
  "crown_sentence": "一势给空间，两户给价值，三链给规模，四垒给时间。",
  "stages": []
}
```

- [ ] **Step 2: Populate B1 with the exact typed contract**

Append this stage object:

```json
{
  "id": "B1",
  "canon_action": "原力借势",
  "structural_projection": "一大势",
  "economic_dimension": "value_space",
  "human_dimension": "空间",
  "first_principles_question": "未来十年，新增价值会在哪里大量产生？",
  "output_state": "opportunity",
  "output_asset": "strategic_field",
  "machine_fields": ["world_transition", "value_pool", "why_now", "runway_hypothesis", "founder_asymmetry", "invalidators"],
  "forbidden_reductions": ["sector_hotness", "trend_without_founder_fit"],
  "human_compression": "一势给空间"
}
```

- [ ] **Step 3: Populate B2 without replacing the four psychological accounts**

Append this stage object:

```json
{
  "id": "B2",
  "canon_action": "品类独创",
  "structural_projection": "两账户",
  "economic_dimension": "value_density",
  "human_dimension": "价值",
  "first_principles_question": "用户为什么愿意把自己的预算分配给我们？",
  "output_state": "demand_asset",
  "strategic_value_accounts": {
    "functional": {"label": "功能账户", "logic": "cost_logic", "strategy": "极致性价比"},
    "value": {"label": "价值账户", "logic": "outcome_logic", "strategy": "创新十倍好"}
  },
  "psychological_accounts_preserved": ["功能", "情绪", "社交", "投资"],
  "machine_fields": ["sweet_user", "valuable_job", "value_account", "budget_source", "category_definition", "mental_position", "willingness_to_pay_logic", "invalidators"],
  "forbidden_reductions": ["two_accounts_replace_four_psychological_accounts", "account_equals_price_level"],
  "human_compression": "两户给价值"
}
```

- [ ] **Step 4: Populate B3 with the operating-language and asset-language dual mapping**

Append this stage object:

```json
{
  "id": "B3",
  "canon_action": "模式升维",
  "structural_projection": "三链路",
  "economic_dimension": "value_scale",
  "human_dimension": "规模",
  "first_principles_question": "已经成立的用户价值，能否脱离创始人时间，规模化转化为 Owner Cash Flow？",
  "output_state": "scalable_cashflow_asset",
  "output_asset": "scalable_cashflow_machine",
  "operating_language_preserved": ["前链路", "后链路", "财链路"],
  "human_projection": ["增长链", "复制链", "复利链"],
  "chains": {
    "growth": {"source": "前链路", "label": "增长链", "transition": "demand_to_customer_asset", "output": "customer_asset"},
    "replication": {"source": "后链路", "label": "复制链", "transition": "founder_capability_to_system_asset", "output": "system_asset"},
    "compounding": {"source": "财链路", "label": "复利链", "transition": "profit_to_reinvestable_capital", "output": "capital_asset"}
  },
  "machine_fields": ["growth_chain", "replication_chain", "compounding_chain", "owner_cash_flow_interface", "invalidators"],
  "forbidden_reductions": ["three_departments", "growth_equals_acquisition_only", "replication_equals_sop_only", "compounding_equals_accounting_profit"],
  "human_compression": "三链给规模"
}
```

- [ ] **Step 5: Populate B4 and explicitly preserve the four barriers**

Append this stage object:

```json
{
  "id": "B4",
  "canon_action": "壁垒锁定",
  "structural_projection": "四壁垒",
  "economic_dimension": "value_duration",
  "human_dimension": "时间",
  "first_principles_question": "为什么已经形成的现金流会持续属于我们，并随规模强化？",
  "output_state": "controlled_compounding_asset",
  "barriers_preserved": ["虚", "实", "入", "出"],
  "control_mapping": {
    "虚": "mind_control",
    "实": "supply_control",
    "入": "switching_control",
    "出": "network_ecosystem_control"
  },
  "control_maturity": ["protection", "concentration", "self_reinforcement"],
  "machine_fields": ["mind_control", "supply_control", "switching_control", "network_control", "strategic_control_points", "control_point_function", "substitutability", "self_reinforcement", "invalidators"],
  "forbidden_reductions": ["fifth_barrier", "scalar_moat_score", "static_defense_only"],
  "human_compression": "四垒给时间"
}
```

- [ ] **Step 6: Create the human mother architecture artifact**

Create `trilogy/YEA1-原力创业资产生成母架构-v0.1.md` with these mandatory sections and no extra framework layer:

```text
00｜Authority & Status
01｜Mother Question：一个经营资产如何从机会变成可复利资产？
02｜Four-Step Map：B1–B4 × 一二三四 × 空间价值规模时间
03｜B1 一大势：Value Space
04｜B2 两账户：Value Density
05｜B3 三链路：Value Scale
06｜B4 四壁垒：Value Duration
07｜Asset State Transition
08｜YWA0 Boundary：止于 Owner Free Cash Flow
09｜Forbidden Misreadings
10｜Human Crown Expressions
```

The artifact must visibly include both exact statements:

```text
一势给空间，两户给价值，三链给规模，四垒给时间。
```

```text
去一个越来越大的世界，做一件越来越值钱的事，造一台越来越会赚钱的机器，建立一个越来越难被取代的系统。
```

- [ ] **Step 7: Update state and commit**

Set in `project/yea1/YEA1-STATE-v0.1.yaml`:

```yaml
scope:
  mother_architecture: DONE
  machine_contract: DONE
```

Run:

```bash
python -m json.tool trilogy/_atlas/yea1-entrepreneurship-asset-architecture-v0.1.json >/dev/null
git diff --check
git add trilogy/_atlas/yea1-entrepreneurship-asset-architecture-v0.1.json trilogy/YEA1-原力创业资产生成母架构-v0.1.md project/yea1/YEA1-STATE-v0.1.yaml
git commit -m "docs: add YEA1 asset architecture contract"
```

---

### Task 3: Project YEA1 Additively into Entrepreneurship Atlas and Outline

**Files:**
- Modify: `trilogy/_atlas/atlas-v2-chuangye.json`
- Modify: `trilogy/原力创业-四级目录.md`
- Modify: `project/yea1/YEA1-STATE-v0.1.yaml`

**Interfaces:**
- Consumes: `trilogy/_atlas/yea1-entrepreneurship-asset-architecture-v0.1.json` stage IDs and exact field values.
- Produces: machine retrieval through the existing Entrepreneurship Atlas plus a human projection entry without rewriting the established 51-section body.

- [ ] **Step 1: Add one top-level YEA1 projection block to `atlas-v2-chuangye.json`**

Do not rename existing `domain`, `model`, `第一性问题`, `贯穿`, or existing `chain[*].stage` values. Add this top-level key:

```json
"yea1_projection": {
  "schema": "yuanli.entrepreneurship_asset_architecture.v0.1",
  "status": "CANDIDATE_STRUCTURAL_PROJECTION",
  "source": "trilogy/_atlas/yea1-entrepreneurship-asset-architecture-v0.1.json",
  "structural_projection": ["一大势", "两账户", "三链路", "四壁垒"],
  "human_dimensions": ["空间", "价值", "规模", "时间"],
  "canon_effect": "none"
}
```

- [ ] **Step 2: Add exact additive fields to each of the four existing `chain` nodes**

Map by sequence, never by fuzzy text matching:

```text
seq 1 → B1 / 一大势 / value_space / 空间 / opportunity
seq 2 → B2 / 两账户 / value_density / 价值 / demand_asset
seq 3 → B3 / 三链路 / value_scale / 规模 / scalable_cashflow_asset
seq 4 → B4 / 四壁垒 / value_duration / 时间 / controlled_compounding_asset
```

Add these fields to each node:

```json
"yea1": {
  "id": "B1",
  "structural_projection": "一大势",
  "economic_dimension": "value_space",
  "human_dimension": "空间",
  "output_state": "opportunity",
  "source": "trilogy/_atlas/yea1-entrepreneurship-asset-architecture-v0.1.json",
  "canon_effect": "none"
}
```

Use the corresponding B2/B3/B4 values for the remaining nodes.

- [ ] **Step 3: Add a candidate projection preface to the Markdown outline**

Immediately after the existing five-standard header and before `## 第一关`, insert a new section titled:

```markdown
## YEA1 Candidate Projection｜经营资产生成的第一性结构
```

It must state, in this order:

```text
Canonical actions remain: 借势 → 独创 → 升维 → 锁定
Structural projection: 一大势 → 两账户 → 三链路 → 四壁垒
Economic physics: 空间 → 价值 → 规模 → 时间
Asset states: Opportunity → Demand Asset → Scalable Cashflow Asset → Controlled Compounding Asset
Status: Candidate Projection; Canon effect: none
```

Then include one four-row table with columns:

```text
Canon | Structural Projection | Economic Dimension | Asset Transition | Human Question
```

The four Human Questions must be:

```text
B1：未来十年，新增价值会在哪里大量产生？
B2：用户为什么愿意把自己的预算分配给我们？
B3：已经成立的用户价值，能否脱离创始人时间，规模化转化为 Owner Cash Flow？
B4：为什么已经形成的现金流会持续属于我们，并随规模强化？
```

- [ ] **Step 4: Add the B3 dual-language clarification to the projection preface only**

Include exactly:

```text
前链路 → 增长链 → 需求变成客户资产
后链路 → 复制链 → 个人能力变成系统资产
财链路 → 复利链 → 利润变成可配置资本
```

Do not globally replace `前链路 / 后链路 / 财链路` in the existing outline body.

- [ ] **Step 5: Add the B2 hierarchy clarification**

Include exactly:

```text
功能账户 / 价值账户 = 战略上位压缩
功能 / 情绪 / 社交 / 投资 = 既有心理账户分类，继续保留
```

- [ ] **Step 6: Validate JSON syntax and diff boundaries**

Run:

```bash
python -m json.tool trilogy/_atlas/atlas-v2-chuangye.json >/dev/null
git diff --check
git diff -- trilogy/_atlas/atlas-v2-chuangye.json trilogy/原力创业-四级目录.md
```

Expected: the 51-section body remains present; no existing stage name is renamed; no B5 appears.

- [ ] **Step 7: Update state and commit**

Set:

```yaml
scope:
  atlas_projection: DONE
  outline_projection: DONE
```

Commit:

```bash
git add trilogy/_atlas/atlas-v2-chuangye.json trilogy/原力创业-四级目录.md project/yea1/YEA1-STATE-v0.1.yaml
git commit -m "feat: project YEA1 into entrepreneurship atlas"
```

---

### Task 4: Build the Fail-Closed YEA1 Validator with Tests

**Files:**
- Create: `scripts/yea1/validate_yea1_projection.py`
- Create: `scripts/yea1/test_validate_yea1_projection.py`
- Modify: `project/yea1/YEA1-STATE-v0.1.yaml`

**Interfaces:**
- Consumes: dedicated YEA1 JSON source, projected Atlas, Markdown outline, project state.
- Produces: `validate_repository(root: Path) -> list[str]` and a CLI exit code used by CI.

- [ ] **Step 1: Write unit tests before validator implementation**

Create `scripts/yea1/test_validate_yea1_projection.py` with standard-library `unittest`. The test module must construct minimal temporary JSON/Markdown fixtures and cover these exact failures:

```python
import json
import tempfile
import unittest
from pathlib import Path

from validate_yea1_projection import validate_contract, validate_atlas_projection, validate_outline_text


class YEA1ValidatorTest(unittest.TestCase):
    def test_valid_contract_has_no_errors(self):
        contract = {
            "canon_actions_preserved": ["B1 原力借势", "B2 品类独创", "B3 模式升维", "B4 壁垒锁定"],
            "structural_projection": ["一大势", "两账户", "三链路", "四壁垒"],
            "human_dimensions": ["空间", "价值", "规模", "时间"],
            "stages": [
                {"id": "B1", "canon_action": "原力借势", "structural_projection": "一大势", "economic_dimension": "value_space", "output_state": "opportunity"},
                {"id": "B2", "canon_action": "品类独创", "structural_projection": "两账户", "economic_dimension": "value_density", "output_state": "demand_asset", "psychological_accounts_preserved": ["功能", "情绪", "社交", "投资"]},
                {"id": "B3", "canon_action": "模式升维", "structural_projection": "三链路", "economic_dimension": "value_scale", "output_state": "scalable_cashflow_asset", "operating_language_preserved": ["前链路", "后链路", "财链路"], "human_projection": ["增长链", "复制链", "复利链"]},
                {"id": "B4", "canon_action": "壁垒锁定", "structural_projection": "四壁垒", "economic_dimension": "value_duration", "output_state": "controlled_compounding_asset", "barriers_preserved": ["虚", "实", "入", "出"]}
            ]
        }
        self.assertEqual(validate_contract(contract), [])

    def test_b5_is_rejected(self):
        self.assertTrue(any("B5" in error for error in validate_contract({"canon_actions_preserved": ["B5"], "structural_projection": [], "human_dimensions": [], "stages": []})))

    def test_b2_must_preserve_four_psychological_accounts(self):
        contract = self._valid_contract()
        contract["stages"][1]["psychological_accounts_preserved"] = ["功能", "价值"]
        self.assertTrue(any("psychological" in error for error in validate_contract(contract)))

    def test_b3_must_preserve_operating_language(self):
        contract = self._valid_contract()
        contract["stages"][2]["operating_language_preserved"] = ["增长链", "复制链", "复利链"]
        self.assertTrue(any("前链路" in error for error in validate_contract(contract)))

    def test_b4_rejects_fifth_barrier(self):
        contract = self._valid_contract()
        contract["stages"][3]["barriers_preserved"] = ["虚", "实", "入", "出", "权"]
        self.assertTrue(any("barrier" in error for error in validate_contract(contract)))

    def test_outline_requires_candidate_status(self):
        errors = validate_outline_text("一大势 两账户 三链路 四壁垒")
        self.assertTrue(any("Candidate" in error for error in errors))
```

Implement `_valid_contract()` in the test class by returning the exact object used in `test_valid_contract_has_no_errors`; do not use external fixtures.

- [ ] **Step 2: Run tests and verify the import fails**

Run:

```bash
cd scripts/yea1
python -m unittest -v test_validate_yea1_projection.py
```

Expected: FAIL because `validate_yea1_projection` does not yet exist.

- [ ] **Step 3: Implement pure validation functions**

Create `scripts/yea1/validate_yea1_projection.py` with these public functions:

```python
def validate_contract(contract: dict) -> list[str]: ...
def validate_atlas_projection(contract: dict, atlas: dict) -> list[str]: ...
def validate_outline_text(text: str) -> list[str]: ...
def validate_repository(root: Path) -> list[str]: ...
def main() -> int: ...
```

`validate_contract` must enforce exact values:

```python
EXPECTED_CANON = ["B1 原力借势", "B2 品类独创", "B3 模式升维", "B4 壁垒锁定"]
EXPECTED_STRUCTURAL = ["一大势", "两账户", "三链路", "四壁垒"]
EXPECTED_HUMAN_DIMENSIONS = ["空间", "价值", "规模", "时间"]
EXPECTED_STAGE_MAP = {
    "B1": ("原力借势", "一大势", "value_space", "opportunity"),
    "B2": ("品类独创", "两账户", "value_density", "demand_asset"),
    "B3": ("模式升维", "三链路", "value_scale", "scalable_cashflow_asset"),
    "B4": ("壁垒锁定", "四壁垒", "value_duration", "controlled_compounding_asset")
}
```

Additional invariants:

```text
- reject any stage ID outside B1–B4;
- B2 psychological_accounts_preserved must equal [功能, 情绪, 社交, 投资];
- B3 operating_language_preserved must equal [前链路, 后链路, 财链路];
- B3 human_projection must equal [增长链, 复制链, 复利链];
- B4 barriers_preserved must equal [虚, 实, 入, 出];
- reject keys named score, total_score, composite_score, yea1_score anywhere recursively;
```

`validate_atlas_projection` must verify the Atlas top-level `yea1_projection.source` points to the dedicated contract and each `chain` node with `seq` 1–4 contains the exact YEA1 mapping.

`validate_outline_text` must require these exact strings:

```text
YEA1 Candidate Projection
一大势
两账户
三链路
四壁垒
空间
价值
规模
时间
Candidate Projection
Canon effect: none
前链路 → 增长链
后链路 → 复制链
财链路 → 复利链
```

It must reject the exact phrases:

```text
B5
五壁垒
两账户取代四账户
三链路就是三个部门
```

- [ ] **Step 4: Implement repository-level validation**

`validate_repository(root)` must load:

```text
trilogy/_atlas/yea1-entrepreneurship-asset-architecture-v0.1.json
trilogy/_atlas/atlas-v2-chuangye.json
trilogy/原力创业-四级目录.md
project/yea1/YEA1-STATE-v0.1.yaml
```

Do not add a PyYAML dependency. For the YAML state file, repository validation only needs string assertions for:

```text
program: YEA1
canon_effect / candidate projection boundary represented in project state
merge_authorized: false
```

`main()` prints each error prefixed `YEA1 FAIL:` and exits `1` if any error exists; otherwise print:

```text
YEA1 projection validation: PASS
```

and return `0`.

- [ ] **Step 5: Run unit tests to green**

Run:

```bash
cd scripts/yea1
python -m unittest -v test_validate_yea1_projection.py
```

Expected: all tests PASS.

- [ ] **Step 6: Run repository validation**

From repository root:

```bash
python scripts/yea1/validate_yea1_projection.py
```

Expected:

```text
YEA1 projection validation: PASS
```

- [ ] **Step 7: Update state and commit**

Set:

```yaml
scope:
  validator: DONE
  validator_tests: DONE
```

Commit:

```bash
git add scripts/yea1 project/yea1/YEA1-STATE-v0.1.yaml
git commit -m "test: add YEA1 fail-closed validator"
```

---

### Task 5: Add the YEA1 Exact-Scope CI Gate

**Files:**
- Create: `.github/workflows/yea1-architecture-sync.yml`
- Modify: `project/yea1/YEA1-STATE-v0.1.yaml`

**Interfaces:**
- Consumes: Task 4 validator.
- Produces: GitHub Actions qualification for exact authorized YEA1 scope.

- [ ] **Step 1: Create the workflow with exact trigger paths**

Create `.github/workflows/yea1-architecture-sync.yml`:

```yaml
name: YEA1 Entrepreneurship Asset Architecture Sync

on:
  pull_request:
    paths:
      - 'docs/superpowers/specs/2026-08-23-yea1-entrepreneurship-asset-architecture-sync-design.md'
      - 'docs/superpowers/plans/2026-08-23-yea1-entrepreneurship-asset-architecture-sync.md'
      - 'trilogy/YEA1-原力创业资产生成母架构-v0.1.md'
      - 'trilogy/原力创业-四级目录.md'
      - 'trilogy/_atlas/yea1-entrepreneurship-asset-architecture-v0.1.json'
      - 'trilogy/_atlas/atlas-v2-chuangye.json'
      - 'trilogy/replays/yea1/**'
      - 'scripts/yea1/**'
      - 'project/yea1/**'
      - '.github/workflows/yea1-architecture-sync.yml'
      - 'courses/**'
      - 'lessons/**'
      - 'director/**'
      - 'deck/**'
      - 'exercises/**'
      - 'runtime/**'
  workflow_dispatch:

permissions:
  contents: read

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Unit test YEA1 validator
        run: python -m unittest -v scripts/yea1/test_validate_yea1_projection.py

      - name: Validate YEA1 projection
        run: python scripts/yea1/validate_yea1_projection.py

      - name: Fail closed on YEA1 scope drift
        if: github.event_name == 'pull_request'
        shell: bash
        run: |
          set -euo pipefail
          git config core.quotePath false
          git fetch origin "${{ github.base_ref }}" --depth=1
          changed="$(git diff --name-only "origin/${{ github.base_ref }}...HEAD")"
          printf '%s\n' "$changed"
          allowed='^(docs/superpowers/(specs/2026-08-23-yea1-entrepreneurship-asset-architecture-sync-design\.md|plans/2026-08-23-yea1-entrepreneurship-asset-architecture-sync\.md)|trilogy/YEA1-原力创业资产生成母架构-v0\.1\.md|trilogy/原力创业-四级目录\.md|trilogy/_atlas/(yea1-entrepreneurship-asset-architecture-v0\.1\.json|atlas-v2-chuangye\.json)|trilogy/replays/yea1/.*|scripts/yea1/.*|project/yea1/.*|\.github/workflows/yea1-architecture-sync\.yml)$'
          unexpected="$(printf '%s\n' "$changed" | grep -Ev "$allowed" || true)"
          if [ -n "$unexpected" ]; then
            echo 'YEA1 FAIL: changed files exceed authorized scope:'
            printf '%s\n' "$unexpected"
            exit 1
          fi
          echo 'YEA1 explicit allowlist scope: PASS'

      - name: Assert learner-facing course and runtime isolation
        if: github.event_name == 'pull_request'
        shell: bash
        run: |
          set -euo pipefail
          changed="$(git diff --name-only "origin/${{ github.base_ref }}...HEAD")"
          forbidden='^(courses/|lessons/|director/|deck/|exercises/|runtime/)'
          if printf '%s\n' "$changed" | grep -E "$forbidden"; then
            echo 'YEA1 FAIL: learner-facing course or runtime layer is not authorized.'
            exit 1
          fi
          echo 'YEA1 course/runtime isolation: PASS'

      - name: Reject whitespace errors
        if: github.event_name == 'pull_request'
        run: git diff --check "origin/${{ github.base_ref }}...HEAD"
```

- [ ] **Step 2: Run local equivalents**

Run:

```bash
python -m unittest -v scripts/yea1/test_validate_yea1_projection.py
python scripts/yea1/validate_yea1_projection.py
git diff --check
```

Expected: all PASS.

- [ ] **Step 3: Update state and commit**

Set:

```yaml
scope:
  ci_gate: DONE
```

Commit:

```bash
git add .github/workflows/yea1-architecture-sync.yml project/yea1/YEA1-STATE-v0.1.yaml
git commit -m "ci: add YEA1 architecture gate"
```

---

### Task 6: Execute the Four-Case Replay and Hard-Negative Validation Pack

**Files:**
- Create: `trilogy/replays/yea1/README.md`
- Create: `trilogy/replays/yea1/amazon-pit-replay.md`
- Create: `trilogy/replays/yea1/nvidia-pit-replay.md`
- Create: `trilogy/replays/yea1/maotai-pit-replay.md`
- Create: `trilogy/replays/yea1/webvan-hard-negative.md`
- Modify: `project/yea1/YEA1-STATE-v0.1.yaml`

**Interfaces:**
- Consumes: YEA1 B1–B4 questions; source evidence available to the executing agent.
- Produces: four comparable replay dossiers with explicit evidence boundaries and discrimination findings. No replay may promote YEA1 by itself.

- [ ] **Step 1: Create the replay protocol**

`trilogy/replays/yea1/README.md` must define this exact per-case structure:

```text
0｜Case Identity + PIT Cutoff
1｜Evidence Boundary
2｜B1 Value Space
3｜B2 Value Density
4｜B3 Value Scale
   - Growth Chain
   - Replication Chain
   - Compounding Chain
5｜B4 Value Duration
   - 虚 / 实 / 入 / 出
   - Protection / Concentration / Self-Reinforcement
6｜What Was Knowable at PIT
7｜Hard Negative / Competing Explanation
8｜Invalidators
9｜Ex-Post Outcome (strictly separated from PIT thesis)
10｜YEA1 Discrimination Result
```

Every claim line must be tagged as one of:

```text
[PIT_FACT]
[PIT_INFERENCE]
[EX_POST_OUTCOME]
[UNKNOWN]
```

Rule:

```text
EX_POST_OUTCOME may not be used to upgrade a PIT_FACT or PIT_INFERENCE.
```

- [ ] **Step 2: Build Amazon Gold Replay**

Use PIT cutoff:

```text
2003-12-31
```

Preferred evidence order:

```text
Amazon SEC filings and shareholder letters available by the cutoff
contemporaneous company materials
credible contemporaneous reporting
```

Required YEA1 questions:

```text
B1: Was e-commerce an expanding value space by PIT?
B2: Was Amazon earning a distinct customer budget/mental position rather than only discount demand?
B3 Growth: were repeat purchase, selection, marketplace, or customer relationships increasing future demand quality?
B3 Replication: was fulfillment/software/marketplace infrastructure reducing proportional founder/manual dependence?
B3 Compounding: was the business showing a credible route from gross profit/operating economics toward owner cash generation, even if immature?
B4: which control mechanisms were protection only, concentration, or self-reinforcing?
```

If required contemporaneous evidence is unavailable, mark the affected answer `[UNKNOWN]`; do not import later AWS or advertising outcomes into the 2003 PIT thesis.

- [ ] **Step 3: Build NVIDIA Gold Replay**

Use PIT cutoff:

```text
2022-11-30
```

Preferred evidence order:

```text
NVIDIA filings, earnings materials, CUDA/platform documentation available by the cutoff
credible pre-cutoff technical/ecosystem evidence
```

Required discrimination:

```text
B1: accelerated computing / AI compute value-space expansion knowable before post-ChatGPT price outcomes?
B2: why customer budget could preferentially flow to NVIDIA rather than generic semiconductor exposure?
B3: whether software + hardware + systems created scalable delivery and cash-generation capability?
B4: whether CUDA/ecosystem/supply/system integration functioned as durable control, value concentration, or self-reinforcement?
```

Do not use 2023–2026 financial results as PIT evidence; they belong only in Section 9 `EX_POST_OUTCOME`.

- [ ] **Step 4: Build Kweichow Moutai Gold Replay**

Use PIT cutoff:

```text
2016-12-31
```

Preferred evidence order:

```text
company annual reports available by the cutoff
industry data available by the cutoff
credible contemporaneous brand/channel evidence
```

Required discrimination:

```text
B1: was premium baijiu / high-end consumption a sufficiently expanding or durable value pool?
B2: did the user budget logic reflect only functional consumption or higher-value social/status/investment-like outcomes?
B3: did demand, production/distribution capability, margins and cash conversion support a scalable cashflow machine?
B4: were brand, production scarcity/time, channel relations and social network effects distinct control mechanisms?
```

Record explicitly if a mechanism is durability without value concentration; YEA1 must not label every moat as a right-tail generator.

- [ ] **Step 5: Build Webvan Hard Negative**

Use PIT cutoff:

```text
1999-11-30
```

Preferred evidence order:

```text
Webvan IPO/S-1 materials available by the cutoff
contemporaneous operating metrics and reporting
```

The hard-negative purpose is not to say `internet was false`; it is to test whether YEA1 distinguishes:

```text
B1 strong or plausible value space
from
B2/B3/B4 weak demand economics, replication economics, cash conversion, or control
```

Required final question:

```text
Could a disciplined YEA1 user at PIT have said "big world, weak asset-generation machine" without knowing the bankruptcy outcome?
```

- [ ] **Step 6: Write one matched discrimination summary**

At the end of `README.md`, add a four-row table:

```text
Case | B1 | B2 | B3 | B4 | Strongest Discriminator | Evidence Status
```

Allowed cell states only:

```text
SUPPORTED
MIXED
UNSUPPORTED
UNKNOWN
```

No numeric totals or weighted scores.

- [ ] **Step 7: Update state honestly**

For each replay set one of:

```text
DONE
EVIDENCE_BLOCKED
```

Never set `DONE` if required source evidence was not inspected.

- [ ] **Step 8: Commit**

```bash
git add trilogy/replays/yea1 project/yea1/YEA1-STATE-v0.1.yaml
git commit -m "research: add YEA1 PIT replay pack"
```

---

### Task 7: Prepare Human Review and Promotion Settlement

**Files:**
- Create: `project/yea1/YEA1-HUMAN-REVIEW-CARD-v0.1.md`
- Modify: `project/yea1/YEA1-STATE-v0.1.yaml`

**Interfaces:**
- Consumes: Tasks 1–6 artifacts and validation results.
- Produces: a bounded Human Gate; no automatic promotion.

- [ ] **Step 1: Create the Human Review card**

The review card must ask exactly these seven questions:

```text
Q1｜第一眼是否能理解：一势=空间、两户=价值、三链=规模、四垒=时间？
Q2｜是否仍能清楚区分 B1–B4 Canon action 与 YEA1 structural projection？
Q3｜两账户是否增强了价值判断，而没有抹掉功能/情绪/社交/投资四账户？
Q4｜增长链/复制链/复利链是否让 B3 从“商业模式工具”升级成“资产化机制”，同时仍保留前/后/财链的操作语义？
Q5｜四壁垒是否从静态防御升级为 Value Control，但没有制造第五壁垒或万能评分？
Q6｜Amazon/NVIDIA/茅台/Webvan replay 是否证明 YEA1 至少具有一定 ex-ante discrimination，而不仅是成功者事后解释？
Q7｜是否值得进入上游 Soul 的独立候选 Human Gate？
```

Mandatory boundary checklist:

```text
Soul Canon changed? NO
B1-B4 renamed? NO
B5 created? NO
Course baseline changed? NO
yuanli-invest changed? NO
YBA0 started? NO
Merge authorized? NO
Publication authorized? NO
```

Allowed Human decisions only:

```text
ACCEPT_YEA1_PROJECTION_FOR_UPSTREAM_CANDIDATE
REVISE_YEA1_PROJECTION
REJECT_YEA1_PROJECTION
```

- [ ] **Step 2: Set project state to Human Review Ready only if validation is green**

Before updating state run:

```bash
python -m unittest -v scripts/yea1/test_validate_yea1_projection.py
python scripts/yea1/validate_yea1_projection.py
git diff --check
```

Only if all commands pass and all four replays are `DONE`, set:

```yaml
status: READY_FOR_HUMAN_REVIEW
scope:
  human_review_card: DONE
next_legal_action: HUMAN_REVIEW_YEA1_PROJECTION
```

If any replay is `EVIDENCE_BLOCKED`, use:

```yaml
status: REPLAY_EVIDENCE_BLOCKED
next_legal_action: RESOLVE_REPLAY_EVIDENCE
```

- [ ] **Step 3: Commit**

```bash
git add project/yea1/YEA1-HUMAN-REVIEW-CARD-v0.1.md project/yea1/YEA1-STATE-v0.1.yaml
git commit -m "governance: prepare YEA1 human review"
```

---

### Task 8: Whole-Branch Verification and Draft PR Handoff

**Files:**
- Verify all YEA1 files from Tasks 1–7.
- Create PR only after whole-branch checks pass.

**Interfaces:**
- Consumes: complete implementation branch.
- Produces: a Draft PR suitable for review; does not merge or promote.

- [ ] **Step 1: Run the complete verification suite**

Run from repository root:

```bash
python -m unittest -v scripts/yea1/test_validate_yea1_projection.py
python scripts/yea1/validate_yea1_projection.py
python -m json.tool trilogy/_atlas/yea1-entrepreneurship-asset-architecture-v0.1.json >/dev/null
python -m json.tool trilogy/_atlas/atlas-v2-chuangye.json >/dev/null
git diff --check 1553de3d5a8bdceba29ecd89eb4224d4e5626d15...HEAD
```

Expected: all PASS and no whitespace errors.

- [ ] **Step 2: Verify the authorized file allowlist locally**

Run:

```bash
git diff --name-only 1553de3d5a8bdceba29ecd89eb4224d4e5626d15...HEAD
```

The only allowed paths are:

```text
docs/superpowers/specs/2026-08-23-yea1-entrepreneurship-asset-architecture-sync-design.md
docs/superpowers/plans/2026-08-23-yea1-entrepreneurship-asset-architecture-sync.md
project/yea1/**
trilogy/YEA1-原力创业资产生成母架构-v0.1.md
trilogy/原力创业-四级目录.md
trilogy/_atlas/yea1-entrepreneurship-asset-architecture-v0.1.json
trilogy/_atlas/atlas-v2-chuangye.json
trilogy/replays/yea1/**
scripts/yea1/**
.github/workflows/yea1-architecture-sync.yml
```

If any `courses/`, `lessons/`, `director/`, `deck/`, `exercises/`, `runtime/`, private-repo, Soul, or `yuanli-invest` path appears, stop and remove it from this branch.

- [ ] **Step 3: Inspect the four non-negotiable semantic invariants manually**

Run:

```bash
grep -n "B1 原力借势\|B2 品类独创\|B3 模式升维\|B4 壁垒锁定" trilogy/YEA1-原力创业资产生成母架构-v0.1.md trilogy/原力创业-四级目录.md
grep -n "前链路\|后链路\|财链路\|增长链\|复制链\|复利链" trilogy/YEA1-原力创业资产生成母架构-v0.1.md trilogy/原力创业-四级目录.md
grep -n "功能\|情绪\|社交\|投资\|功能账户\|价值账户" trilogy/YEA1-原力创业资产生成母架构-v0.1.md trilogy/原力创业-四级目录.md
grep -n "虚\|实\|入\|出" trilogy/YEA1-原力创业资产生成母架构-v0.1.md trilogy/原力创业-四级目录.md
```

Expected: both old and new language coexist with explicit hierarchy; nothing has been silently replaced.

- [ ] **Step 4: Update project state with exact verification evidence**

Record the actual current HEAD and check results in `project/yea1/YEA1-STATE-v0.1.yaml`:

```yaml
verification:
  unit_tests: PASS
  projection_validator: PASS
  json_contract: PASS
  atlas_json: PASS
  diff_check: PASS
  exact_head: <actual git rev-parse HEAD>
```

Do not write a guessed SHA; copy the output of:

```bash
git rev-parse HEAD
```

- [ ] **Step 5: Commit the final state receipt**

```bash
git add project/yea1/YEA1-STATE-v0.1.yaml
git commit -m "governance: record YEA1 exact-head qualification"
```

Then rerun the full verification suite because the exact HEAD changed.

- [ ] **Step 6: Create a Draft PR, not a merge-ready promotion PR**

PR title:

```text
YEA1｜Entrepreneurship Asset Architecture Projection
```

PR body must state:

```text
Status: READY_FOR_HUMAN_REVIEW or REPLAY_EVIDENCE_BLOCKED
Canon effect: none
B1-B4 renamed: no
B5 created: no
Course baseline changed: no
yuanli-invest changed: no
YBA0 started: no
Merge authorized: no
Publication authorized: no
```

Include the exact-head SHA and CI status once GitHub Actions completes.

- [ ] **Step 7: Stop at the Human Gate**

Do not:

```text
mark Soul Canon updated;
merge the PR;
rewrite course baselines;
rebuild/publish portal pages;
start YBA0;
modify yuanli-invest;
claim YEA1 is validated Canon.
```

The only legal next move is the Human decision from Task 7.

---

## Self-Review Against the Accepted Spec

**Spec coverage**

- Authority Constitution → Tasks 1, 5, 7, 8.
- First-principles architecture → Task 2.
- B1/B2/B3/B4 crosswalk → Tasks 2 and 3.
- Two-account / four-psychological-account compatibility → Tasks 2–4.
- Three-chain operating vs human projection compatibility → Tasks 2–4.
- Four-barrier preservation and control maturity → Tasks 2–4.
- YWA0 and YBA0 boundaries → mother architecture plus validator/non-goals; no downstream repo modification.
- Machine-readable crosswalk → Tasks 2–4.
- Replay / Hard Negative → Task 6.
- Governance / Human Gate → Tasks 1, 5, 7, 8.
- No learner-facing baseline overwrite → CI scope isolation in Task 5 and allowlist in Task 8.

**Placeholder scan**

The plan contains no `TBD`, `TODO`, “implement later”, or unspecified test instruction. The only runtime-substituted value is `<actual git rev-parse HEAD>`, and the exact command that supplies it is mandatory immediately before writing the state receipt.

**Type/name consistency**

The exact stage mapping is used consistently throughout:

```text
B1 → 一大势 → value_space → opportunity
B2 → 两账户 → value_density → demand_asset
B3 → 三链路 → value_scale → scalable_cashflow_asset
B4 → 四壁垒 → value_duration → controlled_compounding_asset
```

The dedicated JSON source is always:

```text
trilogy/_atlas/yea1-entrepreneurship-asset-architecture-v0.1.json
```

and all Atlas projections must point back to that source.
