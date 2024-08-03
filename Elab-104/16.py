# ตัวอย่าง Input/Output 1
# Enter n of series: 10
# Alternating Sum from 1 to 10 is -5

# ตัวอย่าง Input/Output 2
# Enter n of series: 15
# Alternating Sum from 1 to 15 is 8


def alter(n):
    global ans
    ans = 0
    for i in range(1,n+1):
        if i%2 == 0:
            ans = ans + ((-1)*i)
        elif i%2 != 0:
            ans = ans + i
    return ans

n = int(input("Enter n of series: "))
print("Alternating Sum from 1 to {0} is {1}".format(n,alter(n)))
