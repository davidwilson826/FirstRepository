parens = '()[]{}'

string = input('Enter string? ')

success = True

index = 0
while index < len(string):
    if parens.index(string[index])+1 == parens.index(string[index+1]):
        string = string[:index]+string[index+1:]
    index += 1
    
print(string)