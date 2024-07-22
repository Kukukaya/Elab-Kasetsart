text = input("Enter a string: ")
num = int(input("Enter arrow's size (greater than 0): "))
if num <=0:
    print("Size must be greater than 0.")
    if (num%2) ==0:
        nick = num//2
    elif (num%2) ==1:
        nick = (num//2)+1
    u=1
    i=1
    space = 0
    while i <=num:
        print(" "*space,text,end='\n')
        i = i+1
        space = space+1
    while u <num:
        k = nick-1
        j=1
        print(text,end='\n')
        u = u+1
        nick = nick-1
        k = k-1

if (num%2) ==0:
    nick = num//2
    u=1
    i=1
    space = 0
    while i <=nick:
        print(" "*space+text,end='\n')
        i = i+1
        space = space+1
    s2 = nick-1
    nu = nick
    while u <=nick:
        k = nick-1
        print(" "*s2+text,end='\n')
        u = u+1
        nu = nu-1
        k = k-1
        s2 = s2 - 1
elif (num%2) ==1:
    nick = (num//2)+1
    u=1
    i=1
    space = 0
    while i <=nick:
        print(" "*space+text,end='\n')
        i = i+1
        space = space+1
    s2 = nick-2
    nu = nick
    while u <nick:
        k = nick-1
        print(" "*s2+text,end='\n')
        u = u+1
        nu = nu-1
        k = k-1
        s2 = s2 - 1