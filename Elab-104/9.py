def plus(total,value):
    return total + value

def minus(total,value):
    return total - value

gf = 0
bf = 0

n_food = int(input("How many food you have : "))
# i = 0 1 2 3 4 ...
for i in range(n_food):
    food , st = input("").split(" ")
    food = int(food)
    st = int(st)
    if st == 1:
        gf = plus(gf,food)
    elif st == -1:
        bf = plus(bf,food)

dif = gf-bf
print(dif)