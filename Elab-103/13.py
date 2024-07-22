# Example1
# Input p: -1
# Fraction = 0

# Example2
# Input p: 0
# Fraction = 10

def fraction(x):
    k =  (2*(x**4)) - (5*(x**3)) -(24*(x**2))-(7*x)+10
    return k

domain = int(input("Input p: "))
frac = fraction(domain)
print(f"Fraction = {frac}")