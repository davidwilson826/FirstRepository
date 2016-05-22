string = input('Enter string? ')

success = True

while len(string) > 0 and success == True:
    length = len(string)
    for x in ['()','[]','{}']:
        if x in string:
            loc = string.index(x)
            string = string[:loc]+string[loc+2:]
    if length == len(string):
        success = False
        
print(success)