from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "courses" / "原力战略三部曲通识课-v1"

FILES = {
    "lesson": COURSE / "lessons" / "B0-原力创业四关.md",
    "exercise": COURSE / "exercises" / "原力创业四关诊断卡.md",
    "deck": COURSE / "deck" / "B0-原力创业四关-PPT蓝图.md",
    "evidence": COURSE / "evidence" / "B0-原力创业四关-证据计划.md",
    "evolution": COURSE / "evolution" / "B0-原力创业四关-Evolution-Note.md",
    "trial": COURSE / "trials" / "B0-原力创业四关-桌面试跑报告.md",
    "control": COURSE / "00-课程总控.md",
}


class B0CoursePackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = {
            name: path.read_text(encoding="utf-8")
            for name, path in FILES.items()
        }

    def test_required_course_assets_exist(self):
        for name, path in FILES.items():
            self.assertTrue(path.exists(), f"missing {name}: {path}")

    def test_b0_is_navigation_not_fifth_canon_module(self):
        lesson = self.text["lesson"]
        control = self.text["control"]
        self.assertIn("不得据此把 B0 升格为第五个正典模块", lesson)
        self.assertIn("不是第五个正典模块", control)
        self.assertIn("临时挂靠 B1", lesson)

    def test_teaching_labels_map_to_canon(self):
        lesson = self.text["lesson"]
        expected = (
            "一势 → 两账 → 三链 → 四权",
            "B1 原力借势",
            "B2 品类独创",
            "B3 模式升维",
            "B4 壁垒锁定",
        )
        for phrase in expected:
            self.assertIn(phrase, lesson)

    def test_two_accounts_boundary_is_explicit(self):
        for name in ("lesson", "exercise", "deck"):
            text = self.text[name]
            self.assertIn("存量账户", text)
            self.assertIn("增量账户", text)
        self.assertIn("两账是两种价值竞争路线", self.text["evidence"])
        self.assertIn("不等于 B2 的完整心理账户体系", self.text["lesson"])
        for gate in ("甜用户", "贵任务", "心理账户", "旧品类", "新品类", "入脑表达"):
            self.assertIn(gate, self.text["lesson"])

    def test_three_chains_and_four_rights_are_stable(self):
        lesson = self.text["lesson"]
        for chain in ("前链路", "后链路", "财链路"):
            self.assertIn(chain, lesson)
        for right in ("心智控制权", "交付控制权", "入口控制权", "留存控制权"):
            self.assertIn(right, lesson)
        self.assertIn("飞轮 = 四种控制权相互强化的机制", lesson)
        self.assertIn("原力母体 = 四种控制权持续生成差异的源头", lesson)

    def test_single_artifact_and_30_day_experiment_are_present(self):
        lesson = self.text["lesson"]
        exercise = self.text["exercise"]
        self.assertIn("《原力创业四关诊断卡》＋一项 30 天最小实验", lesson)
        self.assertIn("30 天最小实验", exercise)
        self.assertIn("反证信号", exercise)
        self.assertIn("同分裁决", exercise)

    def test_maturity_claims_are_honest(self):
        evolution = self.text["evolution"]
        trial = self.text["trial"]
        self.assertIn("live_trial: NOT_RUN", evolution)
        self.assertIn("reusable: false", evolution)
        self.assertIn("canon_candidate: false", evolution)
        self.assertIn("真实学员：NOT_RUN", trial)
        self.assertIn("desktop_trial_pass: PASS", trial)


if __name__ == "__main__":
    unittest.main()
