# Sample Output 1
# Input k: 3
# 1! = 1
# 2! = 2
# 3! = 6
# Summation of factorial 1!-3! = 9

# Sample Output 2
# Input k: 5
# 1! = 1
# 2! = 2
# 3! = 6
# 4! = 24
# 5! = 120
# Summation of factorial 1!-5! = 153


def factorial(x):
    ans = 1
    all_fac = []
    for i in range(1,x+1):
        ans = ans*i
        all_fac.append(ans)
        print(f"{i}! = {ans}")
    print(f"Summation of factorial 1!-{x}! = {sum(all_fac)}")


k_fac = int(input("Input k: "))
factorial(k_fac)