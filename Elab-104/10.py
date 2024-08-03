# Example 1
# Distance from starting point(m.): 7
# 5 3 8 6 11 9 5 8 4 7
# Buzz moved 5 set(s)
# Note: เริ่มแรกบัซซี่จะอยู่ที่ตำแหน่ง 0

# Example 2
# Distance from starting point(m.): 0
# 0
# Buzz moved 0 set(s)

# Example 3
# Distance from starting point(m.): -3
# -4 -1 -5 -2 -6 -3
# Buzz moved 3 set(s)

tardis = int(input("Distance from starting point(m.): "))
# Target distance
check = False
p = 0
ss = 0

if tardis == 0:
    print("0")
else:
    while check == False:
        if p < tardis:
            ss +=1
            p = p + 5
            print(p,end=' ')
            p = p-2
            if p == tardis:
                print(p)
                break
            print(p,end=' ')
        elif p > tardis:
            ss+=1
            p = p-4
            print(p,end=' ')
            p = p+3
            if p == tardis:
                print(p)
                break
            print(p,end=' ')
        

print(f"Buzz moved {ss} set(s)")