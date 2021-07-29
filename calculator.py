def add(a,b):
    result = a + b
    print("a + b = ", result)

def sub(a,b):
    result = a - b
    print("a - b = ",result)

def mul(a,b):
    result = a * b
    print("your result: ",result)

def div(a,b):
    result = a / b
    print("a / b = ",result)

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
op = input("Enter your operator: ")

if op == "+":
    add(a, b)

elif op == "-":
    sub(a, b)

elif op == "*":
    mul(a, b)

elif op == "/":
    div(a, b)

else:
    print("Invalid Operator")



