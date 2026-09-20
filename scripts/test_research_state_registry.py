#!/usr/bin/env python3
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_research_state import load_state, render_current_state


class ResearchStateRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.state = load_state()

    def test_generator_is_deterministic(self):
        self.assertEqual(
            render_current_state(self.state),
            render_current_state(self.state),
        )

    def test_verified_frontier_is_not_head_alias(self):
        frontier = self.state["live_frontier"]
        self.assertIn("verified_through", frontier)
        self.assertIn("branch_head_at_generation", frontier)
        self.assertIn("head_policy", frontier)

    def test_no_go_boundaries_are_explicit(self):
        for result in self.state["no_go_results"]:
            self.assertEqual(
                result["claim_polarity"],
                "NEGATIVE_FOR_CANDIDATE_CLASS",
            )
            self.assertTrue(result["negative_claim_boundary"])

    def test_active_fronts_have_obligations(self):
        for front in self.state["fronts"].values():
            self.assertEqual(front["mathematical_status"], "OPEN")
            self.assertTrue(front["obligations"])


if __name__ == "__main__":
    unittest.main()
