# x: 2
# y: 3
# Result is 1620.00

x=float(input("x: "))
y=float(input("y: "))

def func(x,y):
    su = (((x**2)+(y**2)-1)**3)- ((x**2)*(y**3))
    print("Result is","{:.2f}".format(su))

func(x,y)