import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))

from validate_yea1_projection import (  # noqa: E402
    main,
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

    def _run_main_for_repository(self, root):
        output = io.StringIO()
        with patch(
            "validate_yea1_projection.validate_repository",
            side_effect=lambda _root: validate_repository(root),
        ):
            with redirect_stdout(output):
                exit_code = main()
        return exit_code, output.getvalue()

    def _run_cli_subprocess_for_repository(self, root):
        script_path = root / "scripts" / "yea1" / "validate_yea1_projection.py"
        script_path.parent.mkdir(parents=True)
        source_path = Path(__file__).resolve().parent / "validate_yea1_projection.py"
        script_path.write_text(source_path.read_text(encoding="utf-8"), encoding="utf-8")
        env = os.environ.copy()
        existing_python_path = env.get("PYTHONPATH")
        env["PYTHONPATH"] = os.pathsep.join(
            part for part in (str(root), existing_python_path) if part
        )
        return subprocess.run(
            [sys.executable, str(script_path)],
            cwd=root,
            text=True,
            capture_output=True,
            check=False,
            env=env,
        )

    def _assert_invalid_json_fails_repository_and_cli(self, root, relative_path):
        error_prefix = f"invalid JSON in {relative_path}:"
        result = self._run_cli_subprocess_for_repository(root)
        with self.subTest("CLI exit"):
            self.assertEqual(result.returncode, 1)
        with self.subTest("CLI output"):
            self.assertTrue(result.stdout.startswith(f"YEA1 FAIL: {error_prefix}"))
        with self.subTest("CLI stderr"):
            self.assertEqual(result.stderr, "")

        errors = validate_repository(root)
        with self.subTest("repository errors"):
            self.assertEqual(len(errors), 1)
        if errors:
            with self.subTest("repository error path"):
                self.assertTrue(errors[0].startswith(error_prefix))
            with self.subTest("CLI error identity"):
                self.assertEqual(result.stdout, f"YEA1 FAIL: {errors[0]}\n")
        return errors

    def _assert_invalid_contract_json_fails_repository_and_cli(self, root):
        return self._assert_invalid_json_fails_repository_and_cli(
            root,
            "trilogy/_atlas/yea1-entrepreneurship-asset-architecture-v0.1.json",
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

    def test_non_string_stage_id_returns_error(self):
        contract = self._valid_contract()
        contract["stages"][0]["id"] = []
        errors = validate_contract(contract)
        self.assertTrue(any("stage ID must be a string" in error for error in errors))

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

    def test_deep_contract_tree_reports_forbidden_score_key(self):
        contract = self._valid_contract()
        nested = {"yea1_score": 100}
        for _ in range(1200):
            nested = [nested]
        contract["deep"] = nested
        expected_path = "contract.deep" + ("[0]" * 1200) + ".yea1_score"

        self.assertEqual(
            validate_contract(contract),
            [f"forbidden score key: {expected_path}"],
        )

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

    def test_atlas_projection_rejects_non_string_contract_stage_id(self):
        contract = self._valid_contract()
        contract["stages"][0]["id"] = []
        errors = validate_atlas_projection(contract, self._valid_atlas())
        self.assertTrue(
            any("contract stage ID must be a string" in error for error in errors)
        )

    def test_atlas_projection_rejects_invalid_contract_arguments(self):
        invalid_contracts = [None, {}, [], "contract", 1, True]
        for contract in invalid_contracts:
            with self.subTest(contract=repr(contract)):
                errors = validate_atlas_projection(contract, self._valid_atlas())
                self.assertTrue(errors)
                self.assertTrue(
                    any("source contract" in error.lower() for error in errors)
                )

    def test_outline_rejects_forbidden_phrase(self):
        errors = validate_outline_text(self._valid_outline() + "\n五壁垒")
        self.assertTrue(any("五壁垒" in error for error in errors))

    def test_valid_temporary_repository_has_no_errors(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_repository(root)
            self.assertEqual(validate_repository(root), [])

    def test_main_success_prints_exact_pass_and_returns_zero(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_repository(root)
            exit_code, output = self._run_main_for_repository(root)
            self.assertEqual(exit_code, 0)
            self.assertEqual(output, "YEA1 projection validation: PASS\n")

    def test_main_failure_prints_yea1_fail_and_returns_one(self):
        output = io.StringIO()
        with patch(
            "validate_yea1_projection.validate_repository",
            return_value=["representative failure"],
        ):
            with redirect_stdout(output):
                exit_code = main()
        self.assertEqual(exit_code, 1)
        self.assertEqual(output.getvalue(), "YEA1 FAIL: representative failure\n")

    def test_missing_repository_artifact_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_repository(root)
            (root / "trilogy" / "_atlas" / "atlas-v2-chuangye.json").unlink()
            errors = validate_repository(root)
            self.assertTrue(any("missing required file" in error for error in errors))

    def test_invalid_utf8_repository_artifact_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_repository(root)
            contract_path = (
                root
                / "trilogy"
                / "_atlas"
                / "yea1-entrepreneurship-asset-architecture-v0.1.json"
            )
            contract_path.write_bytes(b"\xff")
            errors = validate_repository(root)
            self.assertTrue(
                any(
                    "unable to read" in error
                    and "yea1-entrepreneurship-asset-architecture-v0.1.json" in error
                    for error in errors
                )
            )

    def test_repository_rejects_non_string_contract_stage_id(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_repository(root)
            contract_path = (
                root
                / "trilogy"
                / "_atlas"
                / "yea1-entrepreneurship-asset-architecture-v0.1.json"
            )
            contract = json.loads(contract_path.read_text(encoding="utf-8"))
            contract["stages"][0]["id"] = []
            contract_path.write_text(
                json.dumps(contract, ensure_ascii=False), encoding="utf-8"
            )
            errors = validate_repository(root)
            self.assertTrue(errors)
            self.assertTrue(
                any("stage ID must be a string" in error for error in errors)
            )

    def test_null_contract_fails_repository_and_cli(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_repository(root)
            contract_path = (
                root
                / "trilogy"
                / "_atlas"
                / "yea1-entrepreneurship-asset-architecture-v0.1.json"
            )
            contract_path.write_text("null", encoding="utf-8")
            errors = validate_repository(root)
            exit_code, output = self._run_main_for_repository(root)
            with self.subTest("repository errors"):
                self.assertEqual(errors, ["contract must be a JSON object"])
            with self.subTest("CLI exit"):
                self.assertEqual(exit_code, 1)
            with self.subTest("CLI output"):
                self.assertEqual(
                    output,
                    "YEA1 FAIL: contract must be a JSON object\n",
                )

    def test_null_atlas_fails_repository_and_cli(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_repository(root)
            atlas_path = root / "trilogy" / "_atlas" / "atlas-v2-chuangye.json"
            atlas_path.write_text("null", encoding="utf-8")
            errors = validate_repository(root)
            exit_code, output = self._run_main_for_repository(root)
            with self.subTest("repository errors"):
                self.assertEqual(errors, ["Atlas must be a JSON object"])
            with self.subTest("CLI exit"):
                self.assertEqual(exit_code, 1)
            with self.subTest("CLI output"):
                self.assertEqual(output, "YEA1 FAIL: Atlas must be a JSON object\n")

    def test_repository_rejects_boolean_atlas_seq(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_repository(root)
            atlas_path = root / "trilogy" / "_atlas" / "atlas-v2-chuangye.json"
            atlas = json.loads(atlas_path.read_text(encoding="utf-8"))
            atlas["chain"][0]["seq"] = True
            atlas_path.write_text(
                json.dumps(atlas, ensure_ascii=False), encoding="utf-8"
            )
            errors = validate_repository(root)
            self.assertTrue(
                any("seq must have type int" in error for error in errors)
            )

    def test_repository_rejects_float_atlas_seq(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_repository(root)
            atlas_path = root / "trilogy" / "_atlas" / "atlas-v2-chuangye.json"
            atlas = json.loads(atlas_path.read_text(encoding="utf-8"))
            atlas["chain"][0]["seq"] = 1.0
            atlas_path.write_text(
                json.dumps(atlas, ensure_ascii=False), encoding="utf-8"
            )
            errors = validate_repository(root)
            self.assertTrue(
                any("seq must have type int" in error for error in errors)
            )

    def test_non_finite_nan_contract_json_fails_repository_and_cli(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_repository(root)
            contract_path = (
                root
                / "trilogy"
                / "_atlas"
                / "yea1-entrepreneurship-asset-architecture-v0.1.json"
            )
            contract = self._valid_contract()
            contract["non_finite"] = float("nan")
            contract_path.write_text(
                json.dumps(contract, ensure_ascii=False), encoding="utf-8"
            )
            self._assert_invalid_contract_json_fails_repository_and_cli(root)

    def test_oversized_integer_contract_json_fails_repository_and_cli(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_repository(root)
            contract_path = (
                root
                / "trilogy"
                / "_atlas"
                / "yea1-entrepreneurship-asset-architecture-v0.1.json"
            )
            contract_text = json.dumps(self._valid_contract(), ensure_ascii=False)
            contract_path.write_text(
                contract_text[:-1]
                + ', "oversized_integer": '
                + ("9" * 5000)
                + "}",
                encoding="utf-8",
            )
            self._assert_invalid_contract_json_fails_repository_and_cli(root)

    def test_excessive_nesting_contract_json_fails_repository_and_cli(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_repository(root)
            original_json_loads = json.loads

            def loads_with_temporary_parser_capacity(*args, **kwargs):
                original_limit = sys.getrecursionlimit()
                sys.setrecursionlimit(10000)
                try:
                    return original_json_loads(*args, **kwargs)
                finally:
                    sys.setrecursionlimit(original_limit)

            (root / "sitecustomize.py").write_text(
                "import json\n"
                "import sys\n"
                "_original_loads = json.loads\n"
                "def _loads_with_temporary_parser_capacity(*args, **kwargs):\n"
                "    original_limit = sys.getrecursionlimit()\n"
                "    sys.setrecursionlimit(10000)\n"
                "    try:\n"
                "        return _original_loads(*args, **kwargs)\n"
                "    finally:\n"
                "        sys.setrecursionlimit(original_limit)\n"
                "json.loads = _loads_with_temporary_parser_capacity\n",
                encoding="utf-8",
            )
            contract_path = (
                root
                / "trilogy"
                / "_atlas"
                / "yea1-entrepreneurship-asset-architecture-v0.1.json"
            )
            contract_text = json.dumps(self._valid_contract(), ensure_ascii=False)
            deeply_nested_value = ("[" * 1200) + "0" + ("]" * 1200)
            contract_path.write_text(
                contract_text[:-1]
                + ', "excessive_nesting": '
                + deeply_nested_value
                + "}",
                encoding="utf-8",
            )
            with patch(
                "validate_yea1_projection.json.loads",
                side_effect=loads_with_temporary_parser_capacity,
            ):
                errors = self._assert_invalid_contract_json_fails_repository_and_cli(
                    root
                )
            self.assertEqual(
                errors,
                [
                    "invalid JSON in trilogy/_atlas/"
                    "yea1-entrepreneurship-asset-architecture-v0.1.json: "
                    "maximum JSON nesting depth exceeds 100"
                ],
            )

    def test_positive_exponent_overflow_contract_json_fails_repository_and_cli(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_repository(root)
            relative_path = (
                "trilogy/_atlas/yea1-entrepreneurship-asset-architecture-v0.1.json"
            )
            contract_path = root / relative_path
            contract_text = contract_path.read_text(encoding="utf-8")
            contract_path.write_text(
                contract_text[:-1] + ', "exponent_overflow": 1e400}',
                encoding="utf-8",
            )
            self._assert_invalid_json_fails_repository_and_cli(root, relative_path)

    def test_negative_exponent_overflow_atlas_json_fails_repository_and_cli(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self._write_repository(root)
            relative_path = "trilogy/_atlas/atlas-v2-chuangye.json"
            atlas_path = root / relative_path
            atlas_text = atlas_path.read_text(encoding="utf-8")
            atlas_path.write_text(
                atlas_text[:-1] + ', "exponent_overflow": -1e400}',
                encoding="utf-8",
            )
            self._assert_invalid_json_fails_repository_and_cli(root, relative_path)


if __name__ == "__main__":
    unittest.main()
