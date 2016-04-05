n = int(input("Enter number? "))

factorial = n-1

while factorial > 1:
    n *= factorial
    factorial -= 1

numzeros = 1

while str(n)[-numzeros] == '0':
    numzeros += 1

print(numzeros-1)