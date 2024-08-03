# Example 1
# Day: 15
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610

fibo = [1,1]
day = int(input("Day: "))
for i in range(day-2):
    ad = fibo[i] + fibo[i+1]
    fibo.append(ad)
    
for j in range(day):
    print(fibo[j],end=' ')
