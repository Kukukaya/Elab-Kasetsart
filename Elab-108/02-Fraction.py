import math as m

class Fraction:
    def __init__(self,numerator = 0,denominator=1):
        self.num = numerator // m.gcd(numerator, denominator)
        self.den = denominator // m.gcd(numerator, denominator)
    def evaluate(self):
        if self.den == 0:
            return None
        div = self.num / self.den
        sh_div = f"{div:.2f}"
        return sh_div

    def add(self,n): 
        return Fraction(self.num+(n*self.den), self.den)

    def __add__(self,frac):
        num = self.num * frac.den
        other_num = frac.num * self.den
        den = self.den * frac.den
        return Fraction(num + other_num, den)

    def multiply(self,n):
        return Fraction(self.num * n, self.den)

    def __mul__(self,frac):
        return Fraction(self.num*frac.num, self.den*frac.den)

    # def __toString__(self.):


    def __str__(self):
        if self.num == 0:
            return "0 / 1"
        for i in range(2,500):
            n = self.num
            d = self.den
            if n % i == 0 and d % i == 0 :
                self.num = self.num/i
                self.den = self.den/i
        return f"{int(self.num)} / {int(self.den)}"


print(Fraction(22,14))
print((Fraction(1,2) + Fraction(3,4)).multiply(0))
print((Fraction(22,14) * Fraction(2, 4)).add(1))
print(Fraction(22, 7).multiply(7).multiply(7))