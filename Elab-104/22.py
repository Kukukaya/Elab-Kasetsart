# Example
# Enter list of tuple: 25 12 44 23 21
# Input list: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Output list: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# Enter list of tuple: 411 55 320 48 454
# Input list: [(4, 1, 1), (5, 5), (3, 2, 0), (4, 8), (4, 5, 4)]
# Output list: [(3, 2, 0), (4, 1, 1), (4, 5, 4), (5, 5), (4, 8)]


def convert_tuple(target):
    ls = []
    for a in target:
        # a is single number in list
        sub_ls = [int(d) for d in a] # d is a single digit in number
        ls.append(tuple(sub_ls))
    return ls

def sortlastdigit(first):
    dl = [int(i) for i in first]
    for i in range(len(dl)):
        for j in range(i, len(dl)):
            last1 = dl[i]%10
            last2 = dl[j]%10
            if(last1>last2):
                dl[i], dl[j] = dl[j], dl[i]
    return dl

tl = ()
numl = []
inl = []
outl = []


num = input("Enter list of tuple: ").split(" ")
numl = list(num)

inl = convert_tuple(numl)
o1 = sortlastdigit(numl)
o2 = [str(x) for x in o1]
outl = convert_tuple(o2)

# print(numl)
print("Input list:",inl)
print("Output list:",outl)