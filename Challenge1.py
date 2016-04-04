alpha = "abcdefghijklmnopqrstuvwxyz"

strings = input("Enter two words?" ).split()

result = "true"

for x in alpha:
    if strings[0].count(x) != strings[1].count(x):
        result = "false"
        
print(result)