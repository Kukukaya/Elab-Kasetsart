

# Enter a set of strings: abc xyz aba 1221
# 2


# Enter a set of strings: aa bab cca 1ds1
# 3


def countStr(m):
    count = 0
    for i in m:
        if((len(i)>=2) and (i[0]==i[-1])): 
            count+=1
    return count

txt = input("Enter a set of strings: ")
ls = txt.split(" ")
print(countStr(ls))