import unittest

from ai_dev_agent_demo.app import add, build_status_message, divide


class TestApp(unittest.TestCase):
    def test_build_status_message(self) -> None:
        self.assertEqual(
            build_status_message(),
            "AI dev agent repository is initialized.",
        )

    def test_add_two_positive_integers(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_add_positive_and_negative_integer(self) -> None:
        self.assertEqual(add(2, -3), -1)

    def test_add_two_decimals(self) -> None:
        self.assertEqual(add(2.5, 1.5), 4.0)

    def test_divide_two_integers(self) -> None:
        self.assertEqual(divide(10, 2), 5)

    def test_divide_decimal_result(self) -> None:
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_negative_number(self) -> None:
        self.assertEqual(divide(-6, 2), -3)

    def test_divide_by_zero_raises_error(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

if __name__ == "__main__":
    unittest.main()
