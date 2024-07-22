# x: 14
# y: 51
# She comes at 17:00

x=int(input("x: "))
y=int(input("y: "))
am = (x+y)%24

print("She comes at", str(am) +":00")