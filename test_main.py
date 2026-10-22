import unittest

from main import calculate


class CalculateTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate("2", "3", "+"), 5)

    def test_subtraction(self):
        self.assertEqual(calculate(7, 2, "-"), 5)

    def test_unsupported_operator(self):
        with self.assertRaisesRegex(ValueError, "operator"):
            calculate(2, 3, "*")

    def test_invalid_number(self):
        with self.assertRaisesRegex(ValueError, "operands"):
            calculate("not a number", 3, "+")


if __name__ == "__main__":
    unittest.main()
