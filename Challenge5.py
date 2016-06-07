#n = int(input("Enter number? "))
n = 24

factors = []

for x in range(2,int(n/2)):
    if n%x == 0:
        factors.append(x)