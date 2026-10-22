first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
operator = input("Enter an operator (+ or -): ").strip()

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
else:
    print("Error: operator must be + or -.")
