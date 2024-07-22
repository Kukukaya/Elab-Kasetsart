# ตัวอย่าง Input/Output
# Enter principle: 25000
# Enter interest rate: 3.25
# Enter time: 6.5
# Return money for simple interest calculation is 30281.25 Baht.
# Return money for compound interest calculation is 30776.94 Baht.


def simple_interest(p, r, t):
    return p+(p*(r/100)*t)
    
def compound_interest(p, r, t):
    return p*((1+(r/100))**t)


p = int(input("Enter principle: "))
r = float(input("Enter interest rate: "))
t = float(input("Enter time: "))

print(f'Return money for simple interest calculation is {simple_interest(p, r, t):.2f} Baht.')
print(f'Return money for compound interest calculation is {compound_interest(p, r, t):.2f} Baht.')