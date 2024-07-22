# Input principal amount (P): 10000
# Input annual nominal interest rate (r): 0.08
# Input # of times the interest is compounded per year (n): 12
# Input # of years (t): 10
# Final amount: 22196.40

P = int(input("Input principal amount (P): "))
r = float(input("Input annual nominal interest rate (r): "))
n = int(input("Input # of times the interest is compounded per year (n): "))
t = int(input("Input # of years (t): "))

def bank(P,r,n,t):
    amount = P*((1+(r/n))**(n*t))
    print("Final amount:","{:.2f}".format(amount))

bank(P,r,n,t)