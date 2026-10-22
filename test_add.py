import unittest
from add import add


class TestAdd(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(4, 5), 9)

    def test_negative_numbers(self):
        self.assertEqual(add(-2, 3), 1)

    def test_zero(self):
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(7, 0), 7)


if __name__ == "__main__":
    unittest.main()
