#!/usr/bin/env python3
"""A command-line calculator supporting addition and subtraction only."""

from __future__ import annotations

import sys
from numbers import Real


def calculate(first: float, operator: str, second: float) -> float:
    """Return the result of applying operator to two numbers."""
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    raise ValueError("operator must be '+' or '-'")


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv

    if args:
        if len(args) != 3:
            print("Usage: python calculator.py NUMBER OPERATOR NUMBER", file=sys.stderr)
            return 2
        first_text, operator, second_text = args
    else:
        values = sys.stdin.read().split()
        if len(values) != 3:
            print("Provide two numbers and an operator.", file=sys.stderr)
            return 2
        first_text, operator, second_text = values

    try:
        first = float(first_text)
        second = float(second_text)
        result = calculate(first, operator, second)
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2

    print(int(result) if result.is_integer() else result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
