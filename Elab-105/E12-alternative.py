# Example Test Case 1

# 2 6
# 7
# 10
# 28
# Example Test Case 2

# 7 10
# 3
# 8
# 3
# 6
# 9
# 2
# 4
# 8

def timeclear_zombie(h,z):
    time = sorted(allTime(h))
    timer = 0
    zombieremain = z
    while zombieremain > 0:
        timer += 1
        for i in time:
            if timer % i == 0:
                zombieremain += -1
    return timer

def allTime(h):
    time_zom = []
    for i in range(h):
        t = int(input(""))
        time_zom.append(t)
    return time_zom

n,m = input("").split(" ")
n = int(n)
m = int(m)

print(timeclear_zombie(n,m))
