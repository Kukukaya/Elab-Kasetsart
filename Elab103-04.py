# Weight: 57
# Height: 165
# Your BMI is 20.9 You're in the healthy weight range.

wei = int(input("Weight: "))
hei = int(input("Height: "))
bmi = wei / ((hei/100)**2)

if bmi<18.6:
    print("Your BMI is","%.1f"%(bmi),"You're in the underweight range.")
elif bmi<25 and bmi>= 18.6:
    print("Your BMI is","%.1f"%(bmi),"You're in the healthy weight range.")
elif bmi<30 and bmi>= 25:
    print("Your BMI is","%.1f"%(bmi),"You're in the overweight range.")
elif bmi>= 30:
    print("Your BMI is","%.1f"%(bmi),"You're in the obese range.")