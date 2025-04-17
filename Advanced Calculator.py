# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

print("Advanced calculator")
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
operation = input("Choose operation 1/2/3/4: ")
num1 = float(input("What is the first number: "))
num2 = float(input("What is the second number: "))
if operation == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif operation == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif operation == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif operation == '4':
    print(num1, "/", num2, "\n=", divide(num1, num2))