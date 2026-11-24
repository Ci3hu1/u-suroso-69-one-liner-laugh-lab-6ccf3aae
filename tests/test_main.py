"""Tests for the One-Liner Laugh Lab entry."""

import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import LINE  # noqa: E402


class TestEntry(unittest.TestCase):
    def test_line_within_gate(self):
        self.assertGreaterEqual(len(LINE), 1)
        self.assertLessEqual(len(LINE), 200)
        self.assertTrue(LINE.strip())
        self.assertNotIn("\n", LINE)

    def test_program_writes_entry_txt(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = dict(os.environ, MAKEFUN_OUTPUT_DIR=tmp)
            repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            proc = subprocess.run(
                [sys.executable, os.path.join(repo, "main.py")],
                env=env, capture_output=True, text=True, timeout=30,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr)
            path = os.path.join(tmp, "entry.txt")
            self.assertTrue(os.path.exists(path))
            with open(path, encoding="utf-8") as f:
                content = f.read()
            self.assertEqual(content.strip(), LINE)
            self.assertLessEqual(len(content.strip()), 200)
            # Output must be readable by every user (grader collects as
            # another user): file mode 0644.
            self.assertEqual(oct(os.stat(path).st_mode & 0o777), "0o644")

    def test_deterministic(self):
        with tempfile.TemporaryDirectory() as tmp1, \
                tempfile.TemporaryDirectory() as tmp2:
            repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            for tmp in (tmp1, tmp2):
                env = dict(os.environ, MAKEFUN_OUTPUT_DIR=tmp)
                subprocess.run(
                    [sys.executable, os.path.join(repo, "main.py")],
                    env=env, check=True, capture_output=True, timeout=30,
                )
            with open(os.path.join(tmp1, "entry.txt"), "rb") as f:
                first = f.read()
            with open(os.path.join(tmp2, "entry.txt"), "rb") as f:
                second = f.read()
            self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
