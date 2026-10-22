import contextlib
import io
import unittest

from calculator import calculate, main


class CalculatorTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(2, "+", 3), 5)

    def test_subtraction(self):
        self.assertEqual(calculate(8, "-", 3), 5)

    def test_multiplication(self):
        self.assertEqual(calculate(4, "*", 3), 12)

    def test_division(self):
        self.assertAlmostEqual(calculate(9, "/", 4), 2.25)

    def test_decimal_values(self):
        self.assertAlmostEqual(calculate(1.5, "+", 2.25), 3.75)

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            calculate(2, "%", 3)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(2, "/", 0)

    def test_command_line_output(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            status = main(["10", "-", "4"])
        self.assertEqual(status, 0)
        self.assertEqual(output.getvalue(), "6\n")

    def test_invalid_number(self):
        errors = io.StringIO()
        with contextlib.redirect_stderr(errors):
            status = main(["not-a-number", "+", "2"])
        self.assertEqual(status, 2)
        self.assertIn("could not convert string to float", errors.getvalue())

    def test_command_line_division_by_zero(self):
        errors = io.StringIO()
        with contextlib.redirect_stderr(errors):
            status = main(["2", "/", "0"])
        self.assertEqual(status, 2)
        self.assertIn("division by zero", errors.getvalue())


if __name__ == "__main__":
    unittest.main()
