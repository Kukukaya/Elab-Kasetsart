# Enter total money: 1218
# 500: 2
# 100: 2
#  20: 0
#   5: 3
#   1: 3

def change(m,amount):
    return m//amount

money = int(input("Enter total money: "))
b500 = change(money,500)
remain = money-(b500*500)
b100 = change(money,100)
remain = money-(b100*100)
b20 = change(money,20)
remain = money-(b20*20)
b5 = change(money,5)
remain = money-(b5*5)
b1 = remain

print("500: %d" % b500)
print("100: %d" % b100)
print(" 20: %d" % b20)
print("  5: %d" % b5)
print("  1: %d" % b1)