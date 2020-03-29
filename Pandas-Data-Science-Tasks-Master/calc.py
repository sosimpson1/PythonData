num1 = float(input(" Enter the first Number"))
op = input(" Enter the first operator")
num2 = float(input(" Enter the Second Number"))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 % num2)
else:
    print("Input operator")