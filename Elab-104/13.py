# Example1
# Input distance: 0
# Police distance: 0
# Criminal distance: 102
# Input distance: 100
# Police distance: 100
# Criminal distance: 106
# Input distance: 14
# Police distance: 114
# Criminal distance: 114
# Caught him!

# Example2
# Input distance: 40
# Police distance: 40
# Criminal distance: 102
# Input distance: 35
# Police distance: 75
# Criminal distance: 106
# Input distance: 40
# Police distance: 115
# Criminal distance: 114
# Caught him!


n = 1   #time
cm_d = 98+(2**n)
pl_d = 0
caught = False

while caught == False:
    dis = int(input("Input distance: "))
    pl_d += dis
    cm_d += (2**n)
    print(f"Police distance: {pl_d}")
    print(f"Criminal distance: {cm_d}")
    n += 1
    if pl_d >= cm_d:
        print("Caught him!")
        caught = True
        break