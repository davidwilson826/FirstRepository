n = int(input('Enter number? '))

for x in range(1,n):
    n *= x
    
zeros = 0

while str(n)[-zeros-1] == '0':
    zeros += 1
    
print(zeros)