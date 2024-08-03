# Example1
# Estimated time : 32
# Week1
# Physical therapy : 40
# Weight training : 10
# Fitness training : 0
# Week2
# Physical therapy : 20
# Weight training : 15
# Fitness training : 10
# Week3
# Physical therapy : 10
# Weight training : 25
# Fitness training : 30
# Week4
# Physical therapy : 10
# Weight training : 30
# Fitness training : 40
# Buzzy has recovered in time.

# Example2
# Estimated time : 41
# Week1
# Physical therapy : 20
# Weight training : 0
# Fitness training : 0
# Week2
# Physical therapy : 20
# Weight training : 10
# Fitness training : 10
# Week3
# Physical therapy : 10
# Weight training : 10
# Fitness training : 10
# Week4
# Physical therapy : 30
# Weight training : 20
# Fitness training : 25
# Week5
# Physical therapy : 0
# Weight training : 10
# Fitness training : 40
# Buzzy has not recovered in time.


es = int(input("Estimated time : "))
tres = es*2.5  #therapy time estimate
week_train = es//8
pt = []
wt = []
ft = []
for i in range(week_train):
    print(f"Week{i+1}")
    p = int(input("Physical therapy : "))
    w = int(input("Weight training : "))
    f = int(input("Fitness training : "))
    pt.append(p)
    wt.append(w)
    ft.append(f)

check_pt = sum(pt)
check_wt = sum(wt)
check_ft = sum(ft)

if check_pt >= tres and check_wt >= tres and check_ft >= tres:
    print("Buzzy has recovered in time.")
else:
    print("Buzzy has not recovered in time.")