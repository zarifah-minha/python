def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

try:
    print("Choose an operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter your choice: ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        result = add(num1,num2)
    elif choice == "2":
        result = subtract(num1,num2)
    elif choice == "3":
        result = multiply(num1,num2)
    elif choice == "4":
        result = divide(num1,num2)
    else:
        print(" Invalid choice.")
        result = None

    if result is not None:
        print("result:", result)

except ZeroDivisionError:
    print("ERROR!!!")

except ValueError:
    print("ERROR!! Only number please")

