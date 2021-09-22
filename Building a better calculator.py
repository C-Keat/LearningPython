#this imidiatly converts a number input into a float, there will be a problem if they input anything but a number
num1 = float(input("Enter the first number: "))
op = input("Enter the operator: ")
num2 = float(input("enter the second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("there is an invalid operator")
