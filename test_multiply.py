import unittest
from multiply import multiply

class TestMultiply(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply(4, 5), 20)
    def test_negative_numbers(self):
        self.assertEqual(multiply(-2, 3), -6)
    def test_zero(self):
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(7, 0), 0)

if __name__ == "__main__":
    unittest.main()
