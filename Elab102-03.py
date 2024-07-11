# x: 3
# Operator: +
# y: 2
# 5

x=int(input("x: "))
ope = input("Operator: ")
y = int(input("y: "))
div = x/y

if ope == "+":
    print(x+y)
elif ope == "-":
    print(x-y)
elif ope == "*":
    print(x*y)
elif ope == "/":
    print("%.2f"%(div))
elif ope == "%":
    print(x%y)
else:
    print("Unknown Operator")