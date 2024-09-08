def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Can't divide by zero."

def calculator():
    print("This is a Simple Calculator program")
    print("please select the operation you want to perform:")
    print("Select 1 if it is Addition")
    print("Select 2 if it is Subtraction")
    print("Select 3 if it is Multiplication")
    print("Select 4 if it is Division")
    
    choice = input("Type in your choice here: ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Please type the first number: "))
        num2 = float(input("Please type the second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input, please try again.")

calculator()
