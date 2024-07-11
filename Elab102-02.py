# Enter your age : 18
# You are Adolescence.

"""Child (0-12 years)
Adolescence (13-18 years)
Adult (19-59 years)
Senior Adult (60 years and above)"""

age = int(input("Enter your age : "))

if age<=12 and age>= 0:
    print("You are Child.")
elif age<=18 and age>=13:
    print("You are Adolescence.")
elif age<=59 and age>=19:
    print("You are Adult.")
elif age>=60:
    print("You are Senior Adult.")
