# Example
# Input starting food (S): 197
# Input Paun's eating rate (P): 70
# Input Gane's eating rate (G): 11
# Paun eats 2 time(s)
# Gane eats 5 time(s)
# Remaining 2 for dog

start_food = int(input("Input starting food (S): "))
Paun_rate = int(input("Input Paun's eating rate (P): "))
Gane_rate = int(input("Input Gane's eating rate (G): "))

def eat(S,P,G):
    ratio_P = S // P
    remnant_P = S-(ratio_P*P)
    ratio_G = remnant_P // G
    remnant_G = remnant_P - (ratio_G*G)
    return ratio_P,ratio_G,remnant_G

food = eat(start_food,Paun_rate,Gane_rate)
print(f"Paun eats {food[0]} time(s)")
print(f"Gane eats {food[1]} time(s)")
print(f"Remaining {food[2]} for dog")