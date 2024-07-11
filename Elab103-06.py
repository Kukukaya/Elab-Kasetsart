# Enter buying amount: 4200.0
# Amount due after discount is 3570.00 baht.

buy = float(input("Enter buying amount: "))

if buy < 1000:
    print("Amount due after discount is",buy,"baht.")
elif buy < 3000 and buy >=1000:
    dis = 0.9
    out = buy*dis
    print("Amount due after discount is","%.2f"%(out),"baht.")
elif buy>=3000:
    dis = 0.85
    out = buy*dis
    print("Amount due after discount is","%.2f"%(out),"baht.")