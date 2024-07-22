# Example 1
# Please enter the value of L: 5
# Area is 44.6350

# Example 2
# Please enter the value of L: 12
# Area is 257.0973
import math as m

def MiniHeart(x):
    pi = m.pi
    return (x**2)+(pi*((x/2)**2))

L = int(input("Please enter the value of L: "))
a = MiniHeart(L)
print(f"Area is {a:.4f}")