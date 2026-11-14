def calculate():
    num = int(input("Enter a number: "))
    num1 = int(input("Enter another number: "))
    operetion = input("Enter an operation (+, -, *, /): ")

    match operetion:
        case "+":
            return num + num1
        case "-":
            return num - num1
        case "*":
            return num * num1
        case "/":
            if num1 != 0:
                return num / num1
            else:
                return "Error: Division by zero is not allowed."
        case _:
            return "Error: Invalid operation."

print(calculate())