# Example 1
# Enter number of levels: 2
# What is the bush size? 3
#   *
#  ***
# *****
#   *
#  ***
# *****
# Example 2
# Enter number of levels: 3
# What is the bush size? 5
#     *
#    ***
#   *****
#  *******
# *********
#     *
#    ***
#   *****
#  *******
# *********
#     *
#    ***
#   *****
#  *******
# *********
# Example 3
# Enter number of levels: 4
# What is the bush size? 2
#  *
# ***
#  *
# ***
#  *
# ***
#  *
# ***

def bush_creater(n):
    lastbush = 2*n-1
    space = n-1
    bushPrint = 1
    while bushPrint <= lastbush :
        print(' '*space,end='')
        print('*'*bushPrint,end='')
        print(' '*space)
        bushPrint += 2
        space += -1


lvl = int(input("Enter number of levels: "))
bs = int(input("What is the bush size? "))

for i in range(lvl):
        bush_creater(bs)
