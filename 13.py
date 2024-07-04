# Example 1
# Is Bulotelli injured?(y/n) y
# Not available

# Example 2
# Is Bulotelli injured?(y/n) n
# Is Bulotelli late for the training?(y/n) y
# Did Bulotelli perform well in training?(y/n) n
# Not selected

# Example 3
# Is Bulotelli injured?(y/n) n
# Is Bulotelli late for the training?(y/n) y
# Did Bulotelli perform well in training?(y/n) y
# Substitute

# Example 4
# Is Bulotelli injured?(y/n) n
# Is Bulotelli late for the training?(y/n) n
# Starter

a1 = input("Is Bulotelli injured?(y/n) ")
if a1 == 'y':
    print("Not available")
elif a1 == 'n':
    a2 = input("Is Bulotelli late for the training?(y/n) ")
    if a2 == 'n':
        print("Starter")
    elif a2 == 'y':
        a3 = input("Did Bulotelli perform well in training?(y/n) ")
        if a3 == 'y':
            print("Substitute")
        elif a3 == 'n':
            print("Not selected")