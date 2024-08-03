# Sample output 1
# Input number: 21
# 21 = 1x10^0 + 2x10^1

# Sample output 2
# Input number: 306
# 306 = 6x10^0 + 0x10^1 + 3x10^2

# Sample output 3
# Input number: 12201 
# 12201 = 1x10^0 + 0x10^1 + 2x10^2 + 2x10^3 + 1x10^4

# Sample output 4
# Input number: 2 
# 2 = 2x10^0


def count_digits(number):
    global count
    count = 0
    if number == 0 :
        count = 1
    while number != 0:   
        if number < 0:
            number = number * -1
            count = -1
        else:    
            number = number // 10
        count += 1
    return count

def get_last_digit(n):
    return n%10
   
def get_distribution(number):
    st = ''
    ntar = 0
    count_digits(number)
    if count == 1:
        ntar = get_last_digit(number)
        st = f"{ntar}x10^0"
    else:
        ntar = get_last_digit(number)
        st = f"{ntar}x10^0"
        for i in range(1,count):
            n = number // (10**i)
            ntar = get_last_digit(n)
            st += f" + {ntar}x10^{i}"
        return st

    
number = int(input("Input number: "))
print(f"{number} = {get_distribution(number)}")