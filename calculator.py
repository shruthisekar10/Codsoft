def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

def calculator():
    print("Welcome to Simple Calculator!")
    print("Operations available:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        try:
            choice = int(input("Enter operation choice (1/2/3/4): "))
            if choice in (1, 2, 3, 4):
                break
            else:
                print("Invalid choice. Please enter a valid operation choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        result = add(num1, num2)
        operation = '+'
    elif choice == 2:
        result = subtract(num1, num2)
        operation = '-'
    elif choice == 3:
        result = multiply(num1, num2)
        operation = '*'
    elif choice == 4:
        result = divide(num1, num2)
        operation = '/'

    print(f"\n{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    calculator()