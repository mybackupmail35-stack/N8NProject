"""Perform addition or subtraction from command-line input."""


def calculate(first, second, operator):
    """Return the result of applying operator to two numeric values."""
    if operator not in ("+", "-"):
        raise ValueError("operator must be '+' or '-'")
    try:
        first = float(first)
        second = float(second)
    except (TypeError, ValueError) as error:
        raise ValueError("both operands must be numbers") from error

    return first + second if operator == "+" else first - second


def main():
    try:
        first = input("Enter the first number: ")
        operator = input("Enter an operator (+ or -): ").strip()
        second = input("Enter the second number: ")
        result = calculate(first, second, operator)
    except ValueError as error:
        print(f"Error: {error}")
        return

    print(result)


if __name__ == "__main__":
    main()
