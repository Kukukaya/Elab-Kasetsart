# Sample Output

# Input amount : 11
# You get 1 of 10 Baht Coin
# You get 1 of 1 Baht Coin
# Sample Output

# Input amount : 444
# You get 4 of 100 Baht Banknote
# You get 2 of 20 Baht Banknote
# You get 2 of 2 Baht Coin
# Sample Output

# Input amount : 567
# You get 1 of 500 Baht Banknote
# You get 1 of 50 Baht Banknote
# You get 1 of 10 Baht Coin
# You get 1 of 5 Baht Coin
# You get 1 of 2 Baht Coin
# Sample Output

# Input amount : 15394
# You get 15 of 1000 Baht Banknote
# You get 3 of 100 Baht Banknote
# You get 1 of 50 Baht Banknote
# You get 2 of 20 Baht Banknote
# You get 2 of 2 Baht Coin

#Class building Section
class Coin:
  def __init__(self, value = 1):
    self.value = value

  def __str__(self):
    return f'{self.value} Baht Coin'

class BankNote:
  def __init__(self, value = 20):
    self.value = value

  def __str__(self):
    return f'{self.value} Baht Banknote'


#Testing Section
moneyInput = int(input("Input amount : "))
currency = [1000,500,100,50,20,10,5,2,1]
remain = moneyInput

while remain > 0:
  for i in currency:
    n = remain//i
    if n >= 1:
      if i >= 20:
        print(f"You get {n} of {BankNote(i)}")
        remain = remain - (n*i)
      else:
        print(f"You get {n} of {Coin(i)}")
        remain = remain - (n*i)
        

