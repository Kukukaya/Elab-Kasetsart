# Example 1
# 2
# 5
# 5
# 5
# 5
# 3
# 5
# 8
# 5
# 5
# 0
# 4
# 5

# Example 2
# -2
# 7
# -2
# 100
# -2
# 100
# -2
# -2
# -2
# -2
# 5
# 0
# 4
# -2

# Example 3
# 5
# 2
# -2
# 7
# 8
# 9
# 10
# 0
# 1
# 5
# ในตัวอย่างที่ 3 เลขแต่ละตัวต่างก็ถูกใส่เข้ามาติดต่อกันเพียงครั้งเดียว ดังนั้นโปรแกรมจึงรายงานเฉพาะตัวเลขแรก ซึ่งก็คือเลข 5

# Example 4
# 2
# 7
# 7
# 7
# 2
# 2
# 1
# 2
# 2
# 2
# 0
# 3
# 7


check_0 = False
count = 1
si_count = 1
si = 0
all_number = []

while check_0 == False:
    n = int(input(""))
    all_number.append(n)
    if n == 0:
        check_0 == True
        break

for i in range(len(all_number)):
    if all_number[i] == all_number[i-1]:
        count += 1
    elif si == 0:
        si = all_number[0]
        si_count = 1
    elif all_number[i] != all_number[i-1]:
        count += 1
        if count > si_count and si != 0:
            si_count = count
            si = all_number[i-1]
        elif si ==0:
            si_count = 1
        count = 0
        
if si == all_number[0] and si_count == 2:
    si_count = 1

print(si_count)
print(si)
