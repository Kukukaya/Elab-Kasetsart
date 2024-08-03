# Sample output 1
# Enter number: 21
# There are 2 digits in 21

# Sample output 2
# Enter number: 306
# There are 3 digits in 306

# Sample output 3
# Enter number: 12201 
# There are 5 digits in 12201

# Sample output 4
# Enter number: -41 
# There are 2 digits in -41

# Sample output 5
# Enter number: 0 
# There are 1 digits in 0


n = int(input("Enter number: "))

def int_to_list(n):
    l = []
    while n != 0:
        l = [n % 10] + l
        n = n // 10
    return l

print(int_to_list(n))
digit = len(int_to_list(n))
print(f"There are {digit} digits in {n}")