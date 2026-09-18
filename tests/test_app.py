import unittest

from ai_dev_agent_demo.app import build_status_message


class TestApp(unittest.TestCase):
    def test_build_status_message(self) -> None:
        self.assertEqual(
            build_status_message(),
            "AI dev agent repository is initialized.",
        )


if __name__ == "__main__":
    unittest.main()
