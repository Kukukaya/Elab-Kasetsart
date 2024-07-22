
# Example 1
# How long have Buzz played ?: 390
# Total price is 4410 baht.

# Example 2
# How long have Buzz played ?: 195
# Total price is 2430 baht.

rent_hr = 900
min = int(input("How long have Buzz played ?: "))
if min%60 <= 20:
    hr = min // 60
elif min%60 > 20:
    hr = (min//60)+1

if hr>=2 and hr<4:
    rent_hr = rent_hr*0.9
elif hr>=4 and hr<5:
    rent_hr = rent_hr*0.8
elif hr>=5:
    rent_hr = rent_hr*0.7

rent_sum = rent_hr*hr
print("Total price is",int(rent_sum),"baht.")