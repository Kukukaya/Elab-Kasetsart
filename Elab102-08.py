# 5
# 3
# 1
# 1 3 5

# Example2
# 7
# 4
# 6
# 4 6 7

# Example3
# 0
# -1
# -2
# -2 -1 0

A = int(input(""))
B = int(input(""))
C = int(input(""))
ma = A
mea = B
mi = C

if B>A and B>C:
    ma=B
    if A>C:
        mea = A
        mi = C
    else:
        mea = C
        mi = A
    # print(max)
elif C>A and C>B:
    ma = C
    if A>B:
        mea = A
        mi = B
    else:
        mea = B
        mi = A
    # print(max)
elif A>C and A>B:
    ma = A
    if B>C:
        mea = B
        mi = C
    else:
        mea = C
        mi = B

print(mi,mea,ma)
