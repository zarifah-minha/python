try:
    num1,num2 = eval(input("Please enter two numbers separated by comma:"))
    result = num1/num2
    print("result:", result)

except ValueError:
    print("Enter a valid number.")

except ZeroDivisionError:
    print("Division by zero is error!!")

except SyntaxError:
    print("Comma is missing.")

finally:
    print("It will execute no mater what.")