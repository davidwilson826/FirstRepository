parens = '()[]{}'

string = input('Enter string? ')
length = len(string)

success = True

index = 0
while len(string) > 0 and success == True:
    while index < len(string)-1:
        if parens.index(string[index])+1 == parens.index(string[index+1]):
            string = string[:index]+string[index+2:]
        index += 1
    index = 0
    if len(string) == length:
        success = False
    
print(success)