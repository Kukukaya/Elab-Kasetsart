# Input number: 7
# x
# xx
# xxx
# xxxx
# xxxxx
# xxxxxx
# xxxxxxx
# xxxxxx
# xxxxx
# xxxx
# xxx
# xx
# x

# Example 2
# Input number: 1
# x

# Example 3
# Input number: 10
# Please input odd number
# Input number: 5
# x
# xx
# xxx
# xxxx
# xxxxx
# xxxx
# xxx
# xx

num = int(input("Input number: "))
if (num%2) != 1:
    print("Please input odd number")
    num = int(input("Input number: "))
    if (num%2) != 1:
        print("Please input odd number")
    else:
        nick = num
        u=1
        i=1
        while i <=num:
            j=1
            while j<=i:
                print("x",end='')
                if j == i:
                    print(end='\n')
                j = j+1
            i = i+1
        while u <num:
            k = nick-1
            j=1
            print("x"*k,end='\n')
            u = u+1
            nick = nick-1
            k = k-1
else:
    nick = num
    u=1
    i=1
    while i <=num:
        j=1
        while j<=i:
            print("x",end='')
            if j == i:
                print(end='\n')
            j = j+1
        i = i+1
    while u <num:
        k = nick-1
        j=1
        print("x"*k,end='\n')
        u = u+1
        nick = nick-1
        k = k-1

    