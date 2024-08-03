# Example1
# A: 4
# B: 2
# C: 3
# C

# Example2
# A: 3
# B: 4
# C: 3
# B

def minimum(a,b,c):
    global minnum
    if c <= b and c <=a:
        minnum = c
    elif b <= c and b <=a:
        minnum = b
    elif a <= b and a <=c:
        minnum = a
    return minnum

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

minnum = a
while minnum != 0:
    minnum = minimum(a,b,c)
    if minnum == a:
        a += 1
        b -= 1
        c -= 1
    elif minnum == b:
        b += 1
        a -= 1
        c -= 1
    elif minnum == c:
        c += 1
        b -= 1
        a -= 1
        
if minnum == a:
    print("A")
elif minnum == b:
    print("B")
elif minnum == c:
    print("C")
