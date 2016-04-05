n = input("Enter number? ")

factorial = n-1

while factorial > 1:
    n *= factorial
    factorial -= 1

print(n)