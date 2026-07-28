#!/usr/bin/env bash
set -euo pipefail

AUDIT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COURSE_ROOT="$(cd "$AUDIT_DIR/../.." && pwd)"
: "${SOUL_ROOT:?Set SOUL_ROOT to the yuanli-strategy-soul checkout}"
PYTHON_BIN="${PYTHON_BIN:-$(command -v python3)}"

export AUDIT_DIR COURSE_ROOT SOUL_ROOT

"$PYTHON_BIN" - <<'PY'
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import zipfile
from pathlib import Path

import jsonschema
import yaml


audit = Path(os.environ["AUDIT_DIR"])
course = Path(os.environ["COURSE_ROOT"])
soul = Path(os.environ["SOUL_ROOT"])


def fail(message: str) -> None:
    raise AssertionError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tree_hash(root: Path) -> str:
    chunks: list[bytes] = []
    ignored = {".git", "__pycache__", ".DS_Store"}
    for path in sorted(root.rglob("*")):
        if path.is_symlink() or not path.is_file():
            continue
        rel_parts = path.relative_to(root).parts
        if any(part in ignored for part in rel_parts):
            continue
        chunks.extend((path.relative_to(root).as_posix().encode(), b"\0", path.read_bytes(), b"\0"))
    return hashlib.sha256(b"".join(chunks)).hexdigest()


analysis = json.loads((audit / "analysis.json").read_text())
facts = analysis["facts"]
router = yaml.safe_load((course / "capability-router.yaml").read_text())
card = yaml.safe_load((course / "lessons/L0-原力战略起点诊断工作坊.card.yaml").read_text())
schema = yaml.safe_load((soul / "schemas/concept-lesson-card.schema.yaml").read_text())

jsonschema.validate(card, schema)

required = {
    "stage_id", "trigger", "primary", "fallbacks", "availability",
    "input_contract", "output_contract", "preconditions", "quality_gate",
    "external_write", "receipt", "backwrite_target",
}
stages = router["stages"]
if len(stages) != facts["router_stage_count"]:
    fail("router stage count mismatch")
for index, stage in enumerate(stages, start=1):
    missing = required - set(stage)
    if missing:
        fail(f"stage {index} missing fields: {sorted(missing)}")
    if stage["external_write"] is not False:
        fail(f"stage {stage['stage_id']} external_write must remain false")
if len({stage["stage_id"] for stage in stages}) != len(stages):
    fail("duplicate stage_id")

runtime = router["runtime"]
if runtime["governor_validation_state"] != "unknown":
    fail("governor validation state was incorrectly promoted")
if runtime["identity_conflicts"] != facts["managed_identity_conflicts"]:
    fail("identity conflict count mismatch")

managed_ids = [key for key in router["capabilities"] if key.startswith("zk:skill:") and key in {
    "zk:skill:yuanli-brain-surface",
    "zk:skill:research-design-gate",
    "zk:skill:yuanli-research-max",
    "zk:skill:hv-deep-research",
    "zk:skill:yuanli-narrative-four-beats",
    "zk:skill:yuanli-narrative-course",
    "zk:skill:content-quality-gate",
    "zk:skill:yuanli-narrative-marketing",
    "zk:skill:yuanli-course-video-factory",
}]
if len(managed_ids) != facts["managed_capability_count"] or len(set(managed_ids)) != len(managed_ids):
    fail("managed capability identity mismatch")

content_skill = soul / "skills/yuanli-content-engineering"
observed_tree_hash = tree_hash(content_skill)
declared_tree_hash = router["capabilities"]["repo:skill:yuanli-content-engineering"]["content_hash"]
if observed_tree_hash != declared_tree_hash:
    fail(f"content-engineering hash mismatch: {observed_tree_hash} != {declared_tree_hash}")

activation = json.loads((course / "receipts/00-managed-capability-activation.json").read_text())
if activation["security"]["result"] != "9/9_safe":
    fail("managed safe scan receipt mismatch")
if activation["runtime"]["governor_validation_state"] != "unknown":
    fail("activation receipt promoted governor state")
if activation["projection"]["codex"] != "9/9_current_runtime" or activation["projection"]["claude"] != "9/9_current_runtime":
    fail("dual projection receipt mismatch")

for rel, expected in analysis["asset_hashes"].items():
    path = course / rel
    if not path.is_file():
        fail(f"missing asset: {rel}")
    observed = sha256(path)
    if observed != expected:
        fail(f"asset hash mismatch for {rel}: {observed}")

pptx = course / "assets/原力战略起点诊断工作坊-v2.pptx"
with zipfile.ZipFile(pptx) as zf:
    slide_count = sum(bool(re.fullmatch(r"ppt/slides/slide\d+\.xml", name)) for name in zf.namelist())
if slide_count != facts["ppt_slide_count"] or slide_count > facts["ppt_slide_limit"]:
    fail("PPT slide count gate failed")

xlsx = course / "assets/原力战略试讲观察与七天迁移-v2.xlsx"
with zipfile.ZipFile(xlsx) as zf:
    workbook_xml = zf.read("xl/workbook.xml").decode("utf-8")
sheet_names = set(re.findall(r'<(?:\w+:)?sheet name="([^"]+)"', workbook_xml))
expected_sheets = {"班级总览", "学员评分", "节奏观察", "七天迁移", "说明"}
if sheet_names != expected_sheets or len(sheet_names) != facts["xlsx_sheet_count"]:
    fail(f"XLSX sheet mismatch: {sheet_names}")

asset_receipt = json.loads((course / "receipts/03-asset-validation.json").read_text())
if asset_receipt["status"] != "pass_with_documented_nonblocking_warning":
    fail("asset warning boundary missing")
if next(item for item in asset_receipt["assets"] if item["file"].endswith(".xlsx"))["formula_error_count"] != facts["xlsx_formula_error_count"]:
    fail("formula error receipt mismatch")

research = (course / "research/01-四证包.md").read_text()
if research.count("https://doi.org/") != facts["verified_external_source_count"]:
    fail("verified source count mismatch")

timing = (course / "trials/01-L0-120分钟桌面排练报告.md").read_text()
minutes = [int(match.group(1)) for match in re.finditer(r"^\| S[1-9].*?\|\s*(\d+)\s*\|", timing, re.M)]
if sum(minutes) != facts["desktop_timing_budget_minutes"] or len(minutes) != 9:
    fail(f"timing budget mismatch: {minutes}")

videos = (course / "marketing/02-视频号脚本-3条-草稿.md").read_text()
moments = (course / "marketing/03-朋友圈素材-3组-草稿.md").read_text()
if len(re.findall(r"^## [123]\. ", videos, re.M)) != facts["channels_script_draft_count"]:
    fail("Channels script count mismatch")
if len(re.findall(r"^## 第[一二三]组", moments, re.M)) != facts["moments_set_draft_count"]:
    fail("Moments set count mismatch")

remaining = ["A2", "A3", "A4", "B2", "B3", "B4", "C1", "C2", "C3"]
generated = [name for name in remaining if list((course / "lessons").glob(f"{name}-*"))]
if len(generated) != facts["remaining_module_files_generated"]:
    fail(f"remaining modules were generated: {generated}")

soul_standard = (soul / "docs/YUANLI-CONCEPT-LESSON-CARD-STANDARD-v1.md").read_text()
for term in ("心智控制权", "交付控制权", "入口控制权", "留存控制权"):
    if term not in soul_standard:
        fail(f"B4 canonical term missing: {term}")
for forbidden in ("飞轮控制权", "母体控制权"):
    if forbidden in soul_standard:
        fail(f"B4 forbidden fifth/sixth control found: {forbidden}")

course_text = "\n".join(path.read_text(errors="ignore") for path in course.rglob("*.md"))
for phrase in ("live_trial_pending", "其余九模块：HOLD", "未发布"):
    if phrase not in course_text:
        fail(f"required boundary phrase missing: {phrase}")

if facts["external_write_count"] != 0 or facts["live_trial_class_count"] != 0 or facts["real_learner_count"] != 0:
    fail("false live or external evidence in analysis")

print(json.dumps({
    "status": "verified",
    "router_stages": len(stages),
    "managed_capabilities": len(managed_ids),
    "ppt_slides": slide_count,
    "xlsx_sheets": sorted(sheet_names),
    "timing_budget_minutes": sum(minutes),
    "governor_validation_state": runtime["governor_validation_state"],
    "live_trial": analysis["states"]["course"],
}, ensure_ascii=False, indent=2))
PY
