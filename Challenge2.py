parentheses = input("Enter string?")

result = "true"

for x in parentheses:
    if x == '(' or '{' or '[':
        cut = parenteses
        
'''
test everything in cut to see if it is valid
remove cut from parentheses