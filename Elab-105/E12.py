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
    time = allTime(h)
    time = sorted(time)
    timer = 0
    r = 1
    ratio = z // h
    zombieremain = z
    # timeindiv = []
    # for i in range(h):
    #     timeindiv.append[0]
    timer += time[0]*ratio
    print(f"{timer} + ",end=' ')
    zombieremain = zombieremain-ratio
    for i in range(1,len(time)):
        if time[i]*r <= timer:
            zombieremain = zombieremain - (time[i-1]*ratio)//time[i]
            print(f"{time[i]} + ",end=' ')
    while zombieremain >= 1:
        time_round = time[0]
        r += 1
        zombieremain = zombieremain - 1
        timer += time[0]
        print(f"{time[0]} + ",end=' ')
        time_round += time[0]
        if zombieremain == 0:
            break
        for i in range(len(time)):
            if time[i] <= time_round:
                zombieremain = zombieremain - 1
                timer += time[i]
                time_round = time[i]
                print(f"{time[i]} + ",end=' ')
            if zombieremain == 0:
                break
    print("")
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

leasttime = timeclear_zombie(n,m)
print(leasttime)
