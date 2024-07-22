# A : 40
# B : 60
# X : 120
# Wait : 3600 sec
A = int(input("A : "))
B = int(input("B : "))
X = int(input("X : "))
tb = X/B
ta = X/A
sec = (ta-tb)*60*60

print("Wait :",sec,"sec")