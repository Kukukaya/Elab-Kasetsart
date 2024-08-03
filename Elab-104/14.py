# ตัวอย่างที่ 1
# 1
# 100
# 13
# 1 2 3 4 5 6 7 8 9 10 
# 11 12 24 25 37 38 50 51 63 64 
# 76 77 89 90 

# ตัวอย่างที่ 2
# -50
# 50
# 7
# -50 -38 -37 -36 -24 -23 -22 -10 -9 -8 
# 4 5 6 18 19 20 32 33 34 46 
# 47 48 

# ตัวอย่างที่ 3
# -121
# 121
# 11


st = int(input(""))     #starting number
fi = int(input(""))     #finishing number
p = int(input(""))      #Pause number
sh_num = st  #show number
n = 0   # amount of numbers

for i in range(st,fi+2):
    if sh_num > fi:
        break
    while sh_num % p != 0:
        if sh_num > fi:
            break
        print(sh_num,end=' ')
        n +=1
        if n % 10 == 0:
            print("\n",end='')
        sh_num += 1
    while sh_num % p ==0:
        sh_num += 11
        if sh_num > fi:
            break
        if sh_num % p ==0:
            break
        print(sh_num,end=' ')
        n += 1
        if n % 10 == 0:
            print("\n",end='')
        sh_num += 1

