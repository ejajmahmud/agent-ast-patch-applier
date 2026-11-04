"""Tests for agent-ast-patch-applier."""
import unittest
from agent_ast_patch_applier.applier import ASTPatchApplier


class TestASTPatchApplier(unittest.TestCase):
    def setUp(self):
        self.applier = ASTPatchApplier()

    def test_valid_patch(self):
        orig = "def calc():\n    return 1\n"
        patched, meta = self.applier.apply_patch(orig, "return 1", "return 2")
        self.assertTrue(meta["success"])
        self.assertIn("return 2", patched)

    def test_syntax_error_rejected(self):
        orig = "def calc():\n    return 1\n"
        patched, meta = self.applier.apply_patch(orig, "return 1", "return (broken syntax")
        self.assertFalse(meta["success"])
        self.assertEqual(patched, orig)  # Unaltered rollback


if __name__ == "__main__":
    unittest.main()
