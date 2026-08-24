#!/usr/bin/env python3
import json
import math
from pathlib import Path


EXPECTED_CANON = ["B1 原力借势", "B2 品类独创", "B3 模式升维", "B4 壁垒锁定"]
EXPECTED_STRUCTURAL = ["一大势", "两账户", "三链路", "四壁垒"]
EXPECTED_HUMAN_DIMENSIONS = ["空间", "价值", "规模", "时间"]
EXPECTED_STAGE_MAP = {
    "B1": ("原力借势", "一大势", "value_space", "opportunity"),
    "B2": ("品类独创", "两账户", "value_density", "demand_asset"),
    "B3": ("模式升维", "三链路", "value_scale", "scalable_cashflow_asset"),
    "B4": (
        "壁垒锁定",
        "四壁垒",
        "value_duration",
        "controlled_compounding_asset",
    ),
}

CONTRACT_SOURCE = (
    "trilogy/_atlas/yea1-entrepreneurship-asset-architecture-v0.1.json"
)
FORBIDDEN_SCORE_KEYS = {"score", "total_score", "composite_score", "yea1_score"}
MAX_JSON_NESTING_DEPTH = 100
EXPECTED_B2_ACCOUNTS = ["功能", "情绪", "社交", "投资"]
EXPECTED_B3_OPERATING = ["前链路", "后链路", "财链路"]
EXPECTED_B3_HUMAN = ["增长链", "复制链", "复利链"]
EXPECTED_B4_BARRIERS = ["虚", "实", "入", "出"]


def _reject_non_finite_constant(value):
    raise ValueError(f"non-finite JSON constant is forbidden: {value}")


def _parse_finite_float(value):
    parsed = float(value)
    if not math.isfinite(parsed):
        raise ValueError(f"non-finite JSON number is forbidden: {value}")
    return parsed


def _reject_excessive_json_nesting(text):
    depth = 0
    in_string = False
    escaped = False
    for character in text:
        if in_string:
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == '"':
                in_string = False
            continue

        if character == '"':
            in_string = True
        elif character in "[{":
            depth += 1
            if depth > MAX_JSON_NESTING_DEPTH:
                raise ValueError(
                    "maximum JSON nesting depth exceeds "
                    f"{MAX_JSON_NESTING_DEPTH}"
                )
        elif character in "]}":
            depth -= 1


def _find_forbidden_score_keys(value, path="contract"):
    errors = []
    stack = [(value, path, None)]
    while stack:
        current, current_path, current_key = stack.pop()
        if current_key in FORBIDDEN_SCORE_KEYS:
            errors.append(f"forbidden score key: {current_path}")
        if isinstance(current, dict):
            for key, nested in reversed(tuple(current.items())):
                stack.append((nested, f"{current_path}.{key}", key))
        elif isinstance(current, list):
            for index in range(len(current) - 1, -1, -1):
                stack.append((current[index], f"{current_path}[{index}]", None))
    return errors


def validate_contract(contract: dict) -> list[str]:
    errors = []
    if not isinstance(contract, dict):
        return ["contract must be a JSON object"]

    errors.extend(_find_forbidden_score_keys(contract))

    for key, expected in [
        ("canon_actions_preserved", EXPECTED_CANON),
        ("structural_projection", EXPECTED_STRUCTURAL),
        ("human_dimensions", EXPECTED_HUMAN_DIMENSIONS),
    ]:
        actual = contract.get(key)
        if actual != expected:
            errors.append(f"{key} must equal {expected}; got {actual}")

    stages = contract.get("stages")
    if not isinstance(stages, list):
        errors.append("stages must be a list containing exactly B1-B4")
        return errors

    stage_ids = []
    stages_by_id = {}
    for index, stage in enumerate(stages):
        if not isinstance(stage, dict):
            errors.append(f"stage at index {index} must be an object")
            continue
        stage_id = stage.get("id")
        stage_ids.append(stage_id)
        if not isinstance(stage_id, str):
            errors.append(
                f"contract stage ID must be a string at index {index}; got {stage_id}"
            )
            continue
        if stage_id not in EXPECTED_STAGE_MAP:
            errors.append(f"stage ID outside B1-B4 is forbidden: {stage_id}")
            continue
        if stage_id in stages_by_id:
            errors.append(f"duplicate stage ID: {stage_id}")
            continue
        stages_by_id[stage_id] = stage

    if stage_ids != list(EXPECTED_STAGE_MAP):
        errors.append(
            f"stage IDs must be exactly {list(EXPECTED_STAGE_MAP)}; got {stage_ids}"
        )

    stage_fields = (
        "canon_action",
        "structural_projection",
        "economic_dimension",
        "output_state",
    )
    for stage_id, expected_values in EXPECTED_STAGE_MAP.items():
        stage = stages_by_id.get(stage_id)
        if stage is None:
            errors.append(f"missing required stage: {stage_id}")
            continue
        actual_values = tuple(stage.get(field) for field in stage_fields)
        if actual_values != expected_values:
            errors.append(
                f"{stage_id} mapping must be {expected_values}; got {actual_values}"
            )

    b2 = stages_by_id.get("B2")
    if b2 is not None and b2.get("psychological_accounts_preserved") != EXPECTED_B2_ACCOUNTS:
        errors.append(
            "B2 psychological_accounts_preserved must equal "
            f"{EXPECTED_B2_ACCOUNTS}"
        )

    b3 = stages_by_id.get("B3")
    if b3 is not None:
        if b3.get("operating_language_preserved") != EXPECTED_B3_OPERATING:
            errors.append(
                "B3 operating_language_preserved must equal "
                f"{EXPECTED_B3_OPERATING}"
            )
        if b3.get("human_projection") != EXPECTED_B3_HUMAN:
            errors.append(f"B3 human_projection must equal {EXPECTED_B3_HUMAN}")

    b4 = stages_by_id.get("B4")
    if b4 is not None and b4.get("barriers_preserved") != EXPECTED_B4_BARRIERS:
        errors.append(f"B4 barriers_preserved must equal {EXPECTED_B4_BARRIERS}")

    return errors


def validate_atlas_projection(contract: dict, atlas: dict) -> list[str]:
    contract_errors = validate_contract(contract)
    if contract_errors:
        return [f"source contract invalid: {error}" for error in contract_errors]

    if not isinstance(atlas, dict):
        return ["Atlas must be a JSON object"]

    errors = []
    projection = atlas.get("yea1_projection")
    if not isinstance(projection, dict):
        errors.append("Atlas yea1_projection must be an object")
    elif projection.get("source") != CONTRACT_SOURCE:
        errors.append(
            f"Atlas yea1_projection.source must equal {CONTRACT_SOURCE}; "
            f"got {projection.get('source')}"
        )

    contract_stages = {stage["id"]: stage for stage in contract["stages"]}

    chain = atlas.get("chain")
    if not isinstance(chain, list):
        errors.append("Atlas chain must be a list")
        return errors

    nodes_by_seq = {}
    for node in chain:
        if not isinstance(node, dict):
            errors.append("Atlas chain nodes must be objects")
            continue
        seq = node.get("seq")
        if type(seq) is not int:
            errors.append(f"Atlas chain seq must have type int; got {seq!r}")
            continue
        if seq in range(1, 5):
            if seq in nodes_by_seq:
                errors.append(f"Atlas chain contains duplicate seq {seq}")
            else:
                nodes_by_seq[seq] = node

    for seq, stage_id in enumerate(EXPECTED_STAGE_MAP, start=1):
        node = nodes_by_seq.get(seq)
        if node is None:
            errors.append(f"Atlas chain missing seq {seq} YEA1 mapping")
            continue

        canon_action, _structural, _economic, _output = EXPECTED_STAGE_MAP[stage_id]
        contract_stage = contract_stages[stage_id]
        expected_mapping = {
            "id": stage_id,
            "structural_projection": contract_stage["structural_projection"],
            "economic_dimension": contract_stage["economic_dimension"],
            "human_dimension": EXPECTED_HUMAN_DIMENSIONS[seq - 1],
            "output_state": contract_stage["output_state"],
            "source": CONTRACT_SOURCE,
            "canon_effect": "none",
        }
        if node.get("yea1") != expected_mapping:
            errors.append(
                f"Atlas chain seq {seq} YEA1 mapping must equal "
                f"{expected_mapping}; got {node.get('yea1')}"
            )

        if contract_stage["canon_action"] != canon_action:
            errors.append(
                f"contract stage {stage_id} canon_action must equal {canon_action}"
            )

    return errors


def validate_outline_text(text: str) -> list[str]:
    if not isinstance(text, str):
        return ["outline must be text"]

    required_phrases = [
        "YEA1 Candidate Projection",
        "一大势",
        "两账户",
        "三链路",
        "四壁垒",
        "空间",
        "价值",
        "规模",
        "时间",
        "Candidate Projection",
        "Canon effect: none",
        "前链路 → 增长链",
        "后链路 → 复制链",
        "财链路 → 复利链",
    ]
    forbidden_phrases = ["B5", "五壁垒", "两账户取代四账户", "三链路就是三个部门"]

    errors = []
    for phrase in required_phrases:
        if phrase not in text:
            errors.append(f"outline missing required phrase: {phrase}")
    for phrase in forbidden_phrases:
        if phrase in text:
            errors.append(f"outline contains forbidden phrase: {phrase}")
    return errors


def validate_repository(root: Path) -> list[str]:
    root = Path(root)
    relative_paths = {
        "contract": Path(
            "trilogy/_atlas/yea1-entrepreneurship-asset-architecture-v0.1.json"
        ),
        "atlas": Path("trilogy/_atlas/atlas-v2-chuangye.json"),
        "outline": Path("trilogy/原力创业-四级目录.md"),
        "state": Path("project/yea1/YEA1-STATE-v0.1.yaml"),
    }
    errors = []
    contents = {}

    for name, relative_path in relative_paths.items():
        path = root / relative_path
        if not path.is_file():
            errors.append(f"missing required file: {relative_path}")
            continue
        try:
            contents[name] = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"unable to read {relative_path}: {exc}")

    unparsed = object()
    contract = unparsed
    atlas = unparsed
    for name in ("contract", "atlas"):
        if name not in contents:
            continue
        try:
            _reject_excessive_json_nesting(contents[name])
            parsed = json.loads(
                contents[name],
                parse_constant=_reject_non_finite_constant,
                parse_float=_parse_finite_float,
            )
        except (json.JSONDecodeError, TypeError, ValueError, RecursionError) as exc:
            errors.append(f"invalid JSON in {relative_paths[name]}: {exc}")
            continue
        if name == "contract":
            contract = parsed
        else:
            atlas = parsed

    contract_errors = []
    if contract is not unparsed:
        contract_errors = validate_contract(contract)
        errors.extend(contract_errors)
    if contract is not unparsed and atlas is not unparsed and not contract_errors:
        errors.extend(validate_atlas_projection(contract, atlas))
    if "outline" in contents:
        errors.extend(validate_outline_text(contents["outline"]))
    if "state" in contents:
        state = contents["state"]
        state_phrases = [
            "program: YEA1",
            "candidate_projection_only: true",
            "merge_authorized: false",
        ]
        for phrase in state_phrases:
            if phrase not in state:
                errors.append(f"YEA1 state missing required boundary phrase: {phrase}")

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    errors = validate_repository(root)
    if errors:
        for error in errors:
            print(f"YEA1 FAIL: {error}")
        return 1
    print("YEA1 projection validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
