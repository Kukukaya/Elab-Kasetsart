# Enter a number (0 to 9999): 8143
# Digit place is 3.
# Tens place is 4.
# Hundreds place is 1.
# Thousands place is 8.
# Sum of all digits is 16.

def digit(n):
    return n%10

def tens(n):
    return (n%100)//10

def hundreds(n):
    return (n%1000)//100

def thousands(n):
    return n//1000

def sum_digits(n):
    return digit(n)+tens(n)+hundreds(n)+thousands(n)

n = int(input('Enter a number (0 to 9999): '))
print('Digit place is %d.' % (digit(n)))
print('Tens place is %d.' % (tens(n)))
print('Hundreds place is %d.' % (hundreds(n)))
print('Thousands place is %d.' % (thousands(n)))
print('Sum of all digits is %d.' % (sum_digits(n)))