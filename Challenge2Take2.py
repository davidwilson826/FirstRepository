parens = '()[]{}'

string = input('Enter string? ')

success = True

while len(string) > 0:
    index = 0
    while index < len(string):
        if parens.index(string[index])+1 == parens.index(string[index+1]):