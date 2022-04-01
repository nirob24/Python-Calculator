def add(num1, num2):
    return num1 + num2
 
def subtract(num1, num2):
    return num1 - num2
 
def multiply(num1, num2):
    return num1 * num2
 
def divide(num1, num2):
    return num1 / num2

 
# Take input from the user
operation = input("What you want to do(+, -, *, /, %):")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
 
result = 0
if operation == '+':
    result = add(num1,num2)
elif operation == '-':
    result = subtract(num1,num2)
elif operation == '*':
    result = multiply(num1,num2)
elif operation == '/':
    result = divide(num1,num2)

else:
    print("Please enter: +, -, *, /")
 
print(num1, operation, num2, '=', result)

