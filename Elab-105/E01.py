def isPrime(number):
    flag = True
    if number == 1:
        flag = False
    elif number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                flag = False
                break
    return flag

def printAllPrimes(limit):
    for i in range(1,limit+1):
        if isPrime(i) == True:
            print(i,end=" ")

number = int(input("Input n: "))
printAllPrimes(number)