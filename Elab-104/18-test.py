#Elab ข้อ18 Number of digits
def count_digits(number):
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


number = int(input("Enter number: "))
# digit = len(count_digits(number))
print(f"There are {count_digits(number)} digits in {number}")