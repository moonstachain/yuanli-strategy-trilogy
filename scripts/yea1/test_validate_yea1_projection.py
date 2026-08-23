import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from validate_yea1_projection import (  # noqa: E402
    validate_atlas_projection,
    validate_contract,
    validate_outline_text,
    validate_repository,
)


class YEA1ValidatorTest(unittest.TestCase):
    def _valid_contract(self):
        return {
            "canon_actions_preserved": [
                "B1 原力借势",
                "B2 品类独创",
                "B3 模式升维",
                "B4 壁垒锁定",
            ],
            "structural_projection": ["一大势", "两账户", "三链路", "四壁垒"],
            "human_dimensions": ["空间", "价值", "规模", "时间"],
            "stages": [
                {
                    "id": "B1",
                    "canon_action": "原力借势",
                    "structural_projection": "一大势",
                    "economic_dimension": "value_space",
                    "output_state": "opportunity",
                },
                {
                    "id": "B2",
                    "canon_action": "品类独创",
                    "structural_projection": "两账户",
                    "economic_dimension": "value_density",
                    "output_state": "demand_asset",
                    "psychological_accounts_preserved": ["功能", "情绪", "社交", "投资"],
                },
                {
                    "id": "B3",
                    "canon_action": "模式升维",
                    "structural_projection": "三链路",
                    "economic_dimension": "value_scale",
                    "output_state": "scalable_cashflow_asset",
                    "operating_language_preserved": ["前链路", "后链路", "财链路"],
                    "human_projection": ["增长链", "复制链", "复利链"],
                },
                {
                    "id": "B4",
                    "canon_action": "壁垒锁定",
                    "structural_projection": "四壁垒",
                    "economic_dimension": "value_duration",
                    "output_state": "controlled_compounding_asset",
                    "barriers_preserved": ["虚", "实", "入", "出"],
                },
            ],
        }

    def _valid_atlas(self):
        source = "trilogy/_atlas/yea1-entrepreneurship-asset-architecture-v0.1.json"
        mappings = [
            ("B1", "一大势", "value_space", "空间", "opportunity"),
            ("B2", "两账户", "value_density", "价值", "demand_asset"),
            ("B3", "三链路", "value_scale", "规模", "scalable_cashflow_asset"),
            ("B4", "四壁垒", "value_duration", "时间", "controlled_compounding_asset"),
        ]
        return {
            "yea1_projection": {"source": source},
            "chain": [
                {
                    "seq": seq,
                    "yea1": {
                        "id": stage_id,
                        "structural_projection": structural,
                        "economic_dimension": economic,
                        "human_dimension": human,
                        "output_state": output,
                        "source": source,
                        "canon_effect": "none",
                    },
                }
                for seq, (stage_id, structural, economic, human, output) in enumerate(
                    mappings, start=1
                )
            ],
        }

    def _valid_outline(self):
        return "\n".join(
            [
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
        )

    def _write_repository(self, root):
        atlas_dir = root / "trilogy" / "_atlas"
        atlas_dir.mkdir(parents=True)
        project_dir = root / "project" / "yea1"
        project_dir.mkdir(parents=True)
        (atlas_dir / "yea1-entrepreneurship-asset-architecture-v0.1.json").write_text(
            json.dumps(self._valid_contract(), ensure_ascii=False), encoding="utf-8"
        )
        (atlas_dir / "atlas-v2-chuangye.json").write_text(
            json.dumps(self._valid_atlas(), ensure_ascii=False), encoding="utf-8"
        )
        (root / "trilogy" / "原力创业-四级目录.md").write_text(
            self._valid_outline(), encoding="utf-8"
        )
        (project_dir / "YEA1-STATE-v0.1.yaml").write_text(
            "program: YEA1\npromotion:\n  candidate_projection_only: true\n"
            "  merge_authorized: false\n",
            encoding="utf-8",
        )

    def test_valid_contract_has_no_errors(self):
        self.assertEqual(validate_contract(self._valid_contract()), [])

    def test_b5_is_rejected(self):
        contract = {
            "canon_actions_preserved": ["B5"],
            "structural_projection": [],
            "human_dimensions": [],
            "stages": [],
        }
        self.assertTrue(any("B5" in error for error in validate_contract(contract)))

    def test_b2_must_preserve_four_psychological_accounts(self):
        contract = self._valid_contract()
        contract["stages"][1]["psychological_accounts_preserved"] = ["功能", "价值"]
        self.assertTrue(
            any("psychological" in error for error in validate_contract(contract))
        )

    def test_b3_must_preserve_operating_language(self):
        contract = self._valid_contract()
        contract["stages"][2]["operating_language_preserved"] = [
            "增长链",
            "复制链",
            "复利链",
        ]
        self.assertTrue(any("前链路" in error for error in validate_contract(contract)))

    def test_b4_rejects_fifth_barrier(self):
        contract = self._valid_contract()
        contract["stages"][3]["barriers_preserved"] = ["虚", "实", "入", "出", "权"]
        self.assertTrue(any("barrier" in error for error in validate_contract(contract)))

    def test_outline_requires_candidate_status(self):
        errors = validate_outline_text("一大势 两账户 三链路 四壁垒")
        self.assertTrue(any("Candidate" in error for error in errors))

    def test_recursive_score_key_is_rejected(self):
        contract = self._valid_contract()
        contract["stages"][0]["nested"] = {"yea1_score": 100}
        self.assertTrue(any("yea1_score" in error for error in validate_contract(contract)))

    def test_exact_atlas_projection_has_no_errors(self):
        self.assertEqual(
            validate_atlas_projection(self._valid_contract(), self._valid_atlas()), []
        )

    def test_atlas_projection_rejects_mapping_drift(self):
        atlas = self._valid_atlas()
        atlas["chain"][1]["yea1"]["output_state"] = "score"
        self.assertTrue(
            any(
                "seq 2" in error
                for error in validate_atlas_projection(self._valid_contract(), atlas)
            )
        )

    def test_outline_rejects_forbidden_phrase(self):
        errors = validate_outline_text(self._valid_outline() + "\n五壁垒")
        self.assertTrue(any("五壁垒" in error for error in errors))

    def test_valid_temporary_repository_has_no_errors(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_repository(root)
            self.assertEqual(validate_repository(root), [])

    def test_missing_repository_artifact_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_repository(root)
            (root / "trilogy" / "_atlas" / "atlas-v2-chuangye.json").unlink()
            errors = validate_repository(root)
            self.assertTrue(any("missing required file" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
