# Sample output 1
# Enter positive number: 6 
# Factors of 6 are
# 1 2 3 6
# Sum of 1 2 3 6 is 12
# Number of factors is 4 
# 6 is not prime number.

# Sample output 2
# Enter positive number: 7 
# Factors of 7 are 
# 1 7
# Sum of 1 7 is 8
# Number of factors is 2
# 7 is prime number.


def list_factors(n):
    fac_str = ''
    for i in range(1,n+1):
        if n%i == 0:
            strNum = str(i)
            fac_str += strNum + ' '
    return fac_str
    
def find_sum_and_num_factors(n):
    str_num = list_factors(n)
    sumFac = 0
    for i in str_num:
        if i == ' ':
            continue
        else:
            intNum = int(i)
            sumFac += intNum
    return sumFac

def isPrime(n):
    f = True
    if n == 1:
        show = (f"{n} is not prime number.")
        f = False
    elif n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                show = (f"{n} is not prime number.")
                f = False
                break
        if f == True:
            show = (f"{n} is prime number.")
    return show

def Count_fac(n):
    str_num = list_factors(n)
    count = 0
    for i in str_num:
        if i == ' ':
            continue
        else:
            count += 1
    return count

entNum = int(input("Enter positive number: "))
print(f"Factors of {entNum} are")
print(list_factors(entNum))
print(f"Sum of {list_factors(entNum)}is {find_sum_and_num_factors(entNum)}")
print(f"Number of factors is {Count_fac(entNum)}")
print(isPrime(entNum))

