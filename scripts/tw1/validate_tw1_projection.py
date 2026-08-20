#!/usr/bin/env python3
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
WV = ROOT / "trilogy/_atlas/worldview-v1.json"
PM = ROOT / "portal-map.json"
OVERLAY = ROOT / "trilogy/_atlas/master-outline-worldview-overlay-v1.json"
README = ROOT / "README.md"
SETTLEMENT = ROOT / "trilogy/TW1-LEGACY-EXPLANATION-SETTLEMENT-v0.1.md"
ORIENTATION = ROOT / "trilogy/原力战略三世界-总图.html"
STATE = ROOT / "project/tw1/TW1-STATE-v0.1.yaml"

errors = []
for p in [WV, PM, OVERLAY, README, SETTLEMENT, ORIENTATION, STATE]:
    if not p.exists():
        errors.append(f"missing required file: {p.relative_to(ROOT)}")

if not errors:
    worldview = json.loads(WV.read_text(encoding="utf-8"))
    portal = json.loads(PM.read_text(encoding="utf-8"))
    overlay = json.loads(OVERLAY.read_text(encoding="utf-8"))
    readme = README.read_text(encoding="utf-8")
    settlement = SETTLEMENT.read_text(encoding="utf-8")
    orientation = ORIENTATION.read_text(encoding="utf-8")
    state = STATE.read_text(encoding="utf-8")

    if worldview.get("schema") != "yuanli.trilogy.worldview-projection.v1":
        errors.append("worldview schema drift")
    if worldview.get("program") != "TW1":
        errors.append("program must be TW1")
    if worldview.get("status") != "CANDIDATE_PROJECTION_CONVERGENCE":
        errors.append("TW1 worldview must remain candidate before Human Gate")
    if worldview.get("canon_effect") != "none":
        errors.append("TW1 canon_effect must remain none")

    upstream = worldview.get("upstream") or {}
    if upstream.get("authority_repo") != "moonstachain/yuanli-strategy-soul":
        errors.append("upstream authority repo drift")
    if upstream.get("tw0_merge_commit") != "9441586acb638da9819ff13ca03f7ae68a034dc2":
        errors.append("TW0 merge pin drift")
    if upstream.get("worldview_contract_blob_sha") != "db290e11af9a1c72b219a21ead90e188372cd4bc":
        errors.append("TW0 worldview contract blob pin drift")
    if upstream.get("human_decision") != "ACCEPT_TW0_THREE_WORLDS_WORLDVIEW_CONTRACT":
        errors.append("TW0 Human Acceptance token drift")

    layers = worldview.get("authority_layers") or {}
    if layers.get("canon") != ["原力资产", "原力创业", "原力OS"]:
        errors.append("canonical trilogy names drift")
    if layers.get("architecture") != ["Source", "Venture", "Evolution"]:
        errors.append("architecture layer drift")
    if layers.get("worldview") != ["源头世界", "现实世界", "未来世界"]:
        errors.append("worldview layer drift")
    if layers.get("memory_hook") != "回到源头，进入现实，创造未来。":
        errors.append("memory hook drift")

    worlds = worldview.get("worlds") or []
    expected_ids = ["YL-WORLD-SOURCE", "YL-WORLD-REALITY", "YL-WORLD-FUTURE"]
    if [w.get("id") for w in worlds] != expected_ids:
        errors.append("worlds must be exactly Source / Reality / Future in order")
    if len(worlds) != 3:
        errors.append("world count must be exactly 3")

    if len(worlds) == 3:
        source, reality, future = worlds
        if source.get("canonical_ref") != "YL-A" or source.get("canonical_name") != "原力资产" or source.get("mechanism") != "generation":
            errors.append("Source World mapping drift")
        expected_source_chain = ["原力母体", "A1 发现母体", "A2 回到母体", "A3 获得原力", "A4 显化原力", "原力资产"]
        if source.get("causal_chain") != expected_source_chain:
            errors.append("Source World must preserve Mother → A1-A4 → Asset")

        expected_b = {"B1": "原力借势", "B2": "品类独创", "B3": "模式升维", "B4": "壁垒锁定"}
        if reality.get("canonical_ref") != "YL-B" or reality.get("canonical_name") != "原力创业" or reality.get("mechanism") != "selection":
            errors.append("Reality World mapping drift")
        if reality.get("canonical_modules") != expected_b:
            errors.append("Reality World B1-B4 drift")

        expected_c = {"C1": "一纸文脉", "C2": "一个大脑", "C3": "一张地图", "C4": "一条链路"}
        if future.get("canonical_ref") != "YL-C" or future.get("canonical_name") != "原力OS" or future.get("mechanism") != "retention_evolution":
            errors.append("Future World mapping drift")
        if future.get("canonical_modules") != expected_c:
            errors.append("Future World C1-C4 drift")

    loop = worldview.get("recursive_loop") or {}
    if loop.get("sequence") != ["YL-WORLD-SOURCE", "YL-WORLD-REALITY", "YL-WORLD-FUTURE", "learning_reuse", "YL-WORLD-SOURCE_NEXT"]:
        errors.append("recursive sequence drift")
    if loop.get("compression") != "生成 → 选择 → 继承 → 再生成":
        errors.append("recursive compression drift")

    ai = worldview.get("ai") or {}
    if ai.get("role") != "amplifier":
        errors.append("AI must remain amplifier")
    for key in ["canon_authority", "identity_authority", "decision_authority", "reality_action_authority"]:
        if ai.get(key) is not False:
            errors.append(f"ai.{key} must remain false")

    scope = worldview.get("scope") or {}
    for key in ["changes_soul_canon", "changes_a1_c4", "changes_course_layer", "changes_runtime_authority", "tw2_authorized", "tw3_authorized", "tw4_authorized"]:
        if scope.get(key) is not False:
            errors.append(f"scope.{key} must remain false")

    meta = portal.get("meta") or {}
    if meta.get("worldview_source") != "trilogy/_atlas/worldview-v1.json":
        errors.append("portal worldview source pointer drift")
    if meta.get("upstream_tw0_merge_commit") != upstream.get("tw0_merge_commit"):
        errors.append("portal upstream pin does not match worldview source")
    if meta.get("tagline") != layers.get("memory_hook"):
        errors.append("portal tagline must compile worldview memory hook")
    if "AI" in meta.get("axiom_def", ""):
        errors.append("portal meta axiom may not restore AI as mother relation")

    overview = portal.get("overview") or []
    if not overview or overview[0].get("href") != "trilogy/原力战略三世界-总图.html" or overview[0].get("feature") is not True:
        errors.append("Three Worlds orientation must be first featured portal entry")

    books = portal.get("books") or []
    if len(books) != 3:
        errors.append("portal must expose exactly three canonical books")
    else:
        expected_books = [
            (1, "原力资产", "YL-WORLD-SOURCE", "回到源头", "什么持续生成我的不同？"),
            (2, "原力创业", "YL-WORLD-REALITY", "进入现实", "世界为什么选择、付费并放大这种不同？"),
            (3, "原力OS", "YL-WORLD-FUTURE", "创造未来", "今天发生的价值，怎样被未来继承并继续做功？"),
        ]
        actual = [(b.get("seq"), b.get("name"), b.get("world_id"), b.get("action"), b.get("question")) for b in books]
        if actual != expected_books:
            errors.append("portal book/world/action/question compilation drift")
        for b in books:
            if "U 型理论" in b.get("model", "") or "跨越鸿沟" in b.get("model", "") or "莫比乌斯" in b.get("model", ""):
                errors.append("external legacy model restored as active portal book model")

    if overlay.get("current_worldview_authority") != "trilogy/_atlas/worldview-v1.json":
        errors.append("master outline overlay authority pointer drift")
    if overlay.get("base_may_define_current_trilogy_relation") is not False:
        errors.append("legacy master outline may not define current trilogy relation")
    if overlay.get("base_role") != "DEEP_CONTENT_HISTORICAL_PROJECTION":
        errors.append("legacy master outline role drift")

    required_readme = [
        "正典名负责准确，三个世界负责看懂",
        "回到源头，进入现实，创造未来。",
        "生成 → 选择 → 继承 → 再生成",
        "trilogy/_atlas/worldview-v1.json",
        "TW1 = Projection Convergence",
        "TW2 = Course Overlay",
        "AI = Amplifier",
    ]
    for phrase in required_readme:
        if phrase not in readme:
            errors.append(f"README missing required phrase: {phrase}")

    required_settlement = [
        "主根 / 左腿 / 右腿",
        "EXTERNAL_EXPLANATORY_LENS",
        "LEGACY_AMPLIFICATION_METAPHOR",
        "DEEP_CONTENT / HISTORICAL_PROJECTION",
        "CURRENT_WORLDVIEW_AUTHORITY",
    ]
    for phrase in required_settlement:
        if phrase not in settlement:
            errors.append(f"settlement missing required phrase: {phrase}")

    for phrase in ["YL-WORLD-SOURCE", "YL-WORLD-REALITY", "YL-WORLD-FUTURE", "回到源头，进入现实，创造未来。", "生成 → 选择 → 继承 → 再生成"]:
        if phrase not in orientation:
            errors.append(f"orientation page missing: {phrase}")

    for phrase in [
        "course_layer_changed: false",
        "TW2",
        "NOT_AUTHORIZED",
        "merge_authorized: false",
        "next_state_if_ci_passes: READY_FOR_TW1_HUMAN_REVIEW",
    ]:
        if phrase not in state:
            errors.append(f"TW1 state missing boundary phrase: {phrase}")

if errors:
    print("TW1 Trilogy Projection Convergence: FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("TW1 Trilogy Projection Convergence: PASS")
print("worlds=3")
print("canon_effect=none")
print("upstream_tw0_pinned=true")
print("readme_projection=converged")
print("portal_source=converged")
print("legacy_relation_models=downgraded")
print("course_layer_change=false")
print("TW2=not_authorized")
