# Examples
# Enter the depth of the well: 5
# Enter the height the frog can jump up: 3
# Enter the height the frog slips down: 2
# On day 1 the frog leaps to the depth of 2 meters.
# At night he slips down to the depth of 4 meters.
# On day 2 the frog leaps to the depth of 1 meters.
# At night he slips down to the depth of 3 meters.
# The frog gets out of the well on day 3.

# Enter the depth of the well: 10
# Enter the height the frog can jump up: 8
# Enter the height the frog slips down: 3
# On day 1 the frog leaps to the depth of 2 meters.
# At night he slips down to the depth of 5 meters.
# The frog gets out of the well on day 2.

# Enter the depth of the well: 10
# Enter the height the frog can jump up: 5
# Enter the height the frog slips down: 5
# The frog will never escape from the well.

d = int(input("Enter the depth of the well: "))
h_up = int(input("Enter the height the frog can jump up: "))
h_down = int(input("Enter the height the frog slips down: "))

day = 0
stance = h_up - h_down
leap  = d - h_up
far = d - h_up
check = False

if d - h_up <= 0:
    print("The frog gets out of the well on day 1.")
elif stance == 0 :
    print("The frog will never escape from the well.")
else:
    while check == False:
        day += 1
        print(f"On day {day} the frog leaps to the depth of {far} meters.")
        far = far + h_down
        print(f"At night he slips down to the depth of {far} meters.")
        far = far - h_up
        if far <= 0:
            day += 1
            print(f"The frog gets out of the well on day {day}.")
            check == True
            break
        