reference = ['(',')','{','}','[',']']

parentheses = '[({})]()'#input("Enter string?")

result = "true"

if parentheses[0] in ['(','{','[']:
    print(parentheses[0])
    close = reference[reference.index(parentheses[0])+1]
    print(close)
    cut = parentheses[:parentheses.index(close)+1]
    print(cut)
else:
    result = "false"
    print('hello')
        
'''
test everything in cut to see if it is valid
remove cut from parentheses
'''