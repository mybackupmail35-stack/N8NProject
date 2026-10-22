import unittest
from add_two_numbers import add_two_numbers

class TestAddTwoNumbers(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add_two_numbers(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add_two_numbers(-1, -2), -3)

    def test_mixed_numbers(self):
        self.assertEqual(add_two_numbers(-1, 1), 0)

    def test_zero(self):
        self.assertEqual(add_two_numbers(0, 0), 0)

    def test_float_numbers(self):
        self.assertAlmostEqual(add_two_numbers(2.5, 3.1), 5.6)

if __name__ == '__main__':
    unittest.main()
