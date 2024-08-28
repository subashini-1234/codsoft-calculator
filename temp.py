def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    # Take input from the user
    operation = input("Enter choice (1/2/3/4): ")
    
    if operation not in ['1', '2', '3', '4']:
        print("Invalid input! Please select a valid operation.")
        return
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    if operation == '1':
        print(f"The result is: {add(num1, num2)}")
    elif operation == '2':
        print(f"The result is: {subtract(num1, num2)}")
    elif operation == '3':
        print(f"The result is: {multiply(num1, num2)}")
    elif operation == '4':
        print(f"The result is: {divide(num1, num2)}")

if __name__ == "__main__":
    main()
