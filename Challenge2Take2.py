parens = '()[]{}'

string = input('Enter string? ')
length = len(string)

success = True

index = 0
while len(string) > 0 and success == True:
    while index < len(string):
        if parens.index(string[index])+1 == parens.index(string[index+1]):
            string = string[:index]+string[index+2:]
        index += 1
    if len(string) == length:
        success = False
    
print(string)