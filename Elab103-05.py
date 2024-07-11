# Enter your guess (0 - 100): 111
# Sorry, out of range, try again later.

# Enter your guess (0 - 100): 16
# Sorry, your guess is wrong, try again later.

# Enter your guess (0 - 100): 72
# Congratulations, your guess is correct.

gue = int(input("Enter your guess (0 - 100): "))
target = 72

if gue<0 or gue>100:
    print("Sorry, out of range, try again later.")
elif gue == target:
    print("Congratulations, your guess is correct.")
elif gue != target:
    print("Sorry, your guess is wrong, try again later.")