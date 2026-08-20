#!/usr/bin/env python3
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
OVERLAY = ROOT / "courses/原力战略三部曲通识课-v2/overlays/TW2-THREE-WORLDS-COURSE-OVERLAY-v0.1.md"
TRIAL = ROOT / "courses/原力战略三部曲通识课-v2/trials/11-tw2-three-world-overlay/README.md"
RUBRIC = ROOT / "courses/原力战略三部曲通识课-v2/trials/11-tw2-three-world-overlay/OBSERVATION-RUBRIC-v0.1.md"
SETTLEMENT = ROOT / "courses/原力战略三部曲通识课-v2/trials/11-tw2-three-world-overlay/EVIDENCE-SETTLEMENT-TEMPLATE-v0.1.md"
PROMOTION = ROOT / "courses/原力战略三部曲通识课-v2/trials/11-tw2-three-world-overlay/PROMOTION-GATE-v0.1.md"
STATE = ROOT / "project/tw2/TW2-STATE-v0.1.yaml"

TW1_MERGE = "1553de3d5a8bdceba29ecd89eb4224d4e5626d15"
FROZEN_COURSE_HEAD = "9602583c95ae074a72dce840c297a7ce26abd372"

errors = []
for p in [OVERLAY, TRIAL, RUBRIC, SETTLEMENT, PROMOTION, STATE]:
    if not p.exists():
        errors.append(f"missing required file: {p.relative_to(ROOT)}")

if not errors:
    overlay = OVERLAY.read_text(encoding="utf-8")
    trial = TRIAL.read_text(encoding="utf-8")
    rubric = RUBRIC.read_text(encoding="utf-8")
    settlement = SETTLEMENT.read_text(encoding="utf-8")
    promotion = PROMOTION.read_text(encoding="utf-8")
    state = STATE.read_text(encoding="utf-8")

    required_overlay = [
        "CANDIDATE_LIVE_VALIDATION",
        FROZEN_COURSE_HEAD,
        TW1_MERGE,
        "Ontology Order ≠ Learning Journey",
        "回到源头，进入现实，创造未来。",
        "现实世界 != 赚钱世界",
        "源头世界 != 人格测试世界",
        "未来世界 != AI 世界",
        "M1｜源头世界 = 人格测试 / 人类图 / 星盘？",
        "M2｜现实世界 = 赚钱？",
        "M3｜未来世界 = AI / Agent / 未来科技？",
        "M4｜三个世界 = 三个新的 Canon Part？",
        "M5｜学习顺序 = 正典因果顺序？",
        "correct_three_world_explanation_rate: \">= 0.80\"",
        "self_problem_navigation_rate: \">= 0.70\"",
        "new_parallel_canon_misread_count: 0",
        "existing lesson rewrite",
    ]
    for phrase in required_overlay:
        if phrase not in overlay:
            errors.append(f"overlay missing required contract phrase: {phrase}")

    for phrase in [
        "READY_NOT_RUN",
        "NO_REALITY_EVIDENCE_YET",
        "L0｜自然证据",
        "L1 light validation",
        "Three Worlds improves learning",
    ]:
        if phrase not in trial:
            errors.append(f"trial protocol missing: {phrase}")

    for phrase in ["E0｜未形成", "E3｜能迁移", "N3｜World → Module → Action", "M1｜Source-as-test", "M5｜Journey-equals-ontology", "ADDED_LOAD"]:
        if phrase not in rubric:
            errors.append(f"rubric missing: {phrase}")

    for phrase in ["INSUFFICIENT_EVIDENCE", "PROMOTION_CANDIDATE", "REJECT_BY_REALITY", "correct_three_world_explanation_rate"]:
        if phrase not in settlement:
            errors.append(f"settlement template missing: {phrase}")

    for phrase in ["NOT_ELIGIBLE_BEFORE_REALITY", "REAL_SESSION_OCCURRED", "ACCEPT_TW2_THREE_WORLDS_AS_COURSE_OVERLAY_CANDIDATE"]:
        if phrase not in promotion:
            errors.append(f"promotion gate missing: {phrase}")

    required_state = [
        "status: CANDIDATE_READY_FOR_LIVE_VALIDATION",
        f"trilogy_tw1_merge: {TW1_MERGE}",
        f"frozen_course_head: {FROZEN_COURSE_HEAD}",
        "existing_lesson_files_changed: false",
        "pr18_merge_authorized: false",
        "course_promotion_authorized: false",
        "TW3: NOT_AUTHORIZED",
        "TW4: NOT_AUTHORIZED",
        "lesson_rewrite: NOT_AUTHORIZED",
        "tw2_pr_merge_authorized: false",
        "requires: FRESH_HUMAN_REVIEW_AFTER_REALITY_EVIDENCE",
    ]
    for phrase in required_state:
        if phrase not in state:
            errors.append(f"state missing boundary: {phrase}")

    # Verify TW2 is pinned to the actual merged TW1 machine worldview, not a copied interpretation.
    proc = subprocess.run(
        ["git", "show", f"{TW1_MERGE}:trilogy/_atlas/worldview-v1.json"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        errors.append("cannot read TW1 worldview-v1.json from pinned merge commit")
    else:
        try:
            wv = json.loads(proc.stdout)
            if (wv.get("authority_layers") or {}).get("worldview") != ["源头世界", "现实世界", "未来世界"]:
                errors.append("TW1 world names drift from TW2 assumption")
            if (wv.get("authority_layers") or {}).get("memory_hook") != "回到源头，进入现实，创造未来。":
                errors.append("TW1 memory hook drift from TW2 assumption")
            worlds = wv.get("worlds") or []
            if [w.get("id") for w in worlds] != ["YL-WORLD-SOURCE", "YL-WORLD-REALITY", "YL-WORLD-FUTURE"]:
                errors.append("TW1 world IDs drift")
            if len(worlds) == 3:
                if worlds[0].get("canonical_name") != "原力资产" or worlds[0].get("mechanism") != "generation":
                    errors.append("Source mapping drift")
                if worlds[1].get("canonical_name") != "原力创业" or worlds[1].get("mechanism") != "selection":
                    errors.append("Reality mapping drift")
                if worlds[2].get("canonical_name") != "原力OS" or worlds[2].get("mechanism") != "retention_evolution":
                    errors.append("Future mapping drift")
        except Exception as exc:
            errors.append(f"failed to parse pinned TW1 worldview: {exc}")

if errors:
    print("TW2 Course Three-World Overlay: FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("TW2 Course Three-World Overlay: PASS")
print(f"frozen_course_head={FROZEN_COURSE_HEAD}")
print(f"upstream_tw1_merge={TW1_MERGE}")
print("lesson_rewrite=false")
print("real_session=not_run")
print("promotion=not_authorized")
print("TW3=not_authorized")
print("TW4=not_authorized")
