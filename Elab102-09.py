# Example 1
# Input number: 4
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4

# Example 2
# Input number: 9
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
# 1 2 3 4 5 6 
# 1 2 3 4 5 6 7 
# 1 2 3 4 5 6 7 8 
# 1 2 3 4 5 6 7 8 9 

tri = int(input("Input number: "))
j=1
while j <= tri:
    i=1
    while i <= j:
        if i == j:
            print(i,end="\n")
        elif i<=j:
            print(i,end=' ')
        i = i+1
    j = j+1
        