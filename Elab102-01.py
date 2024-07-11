# Enter initial amount in Baht: 100
# Enter interest rate in percent: 3
# Total amount after 1 year is 103.00 Baht.
# Total amount after 5 years is 115.93 Baht.
# Total amount after 10 years is 134.39 Baht.
# Total amount after 20 years is 180.61 Baht.

dep = int(input("Enter initial amount in Baht: "))
rate = float(input("Enter interest rate in percent: "))

y1 = dep*((1+(rate/100))**1)
y5 = dep*((1+(rate/100))**5)
y10 = dep*((1+(rate/100))**10)
y20 = dep*((1+(rate/100))**20)

print("Total amount after 1 year is",f'{y1:.2f}',"Baht.")
print("Total amount after 5 years is",f'{y5:.2f}',"Baht.")
print("Total amount after 10 years is",f'{y10:.2f}',"Baht.")
print("Total amount after 20 years is",f'{y20:.2f}',"Baht.")
