from math import factorial

#n = int(input("Enter number? "))
n = 24

factors = []

for x in range(2,int(n/2)+1):
    if n%x == 0:
        factors.append(x)
        
print(factors)

possibilities = [factors for x in range(sum(range(len(factors))))]
print(possibilities)

'''
unique = []

for x in possibilities:
    if x not in unique:
        unique.append(x)
        
print(len(unique)+1)
'''