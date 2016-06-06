'''
3 attempts (really lucky)

9 attempts
8 attempts
7 attempts
'''

from random import randint
from time import time

start = time()

number = [str(randint(0,9)) for x in range(5)]
#number = '55890'

attempts = 0
guesses = []

def compare():
    
    def makeGuess():
        global guess
        guess = input("Guess a five digit number. ")#'58995'
        for x in guess:
            #print(x)
            if x not in '0123456789' or len(guess) != 5:
                print('Not a five digit number. Try again.')
                makeGuess()
                return
                
    makeGuess()
    
    global attempts
    attempts += 1
    
    nfreq = [number.count(str(x)) for x in range(10)]
    gfreq = [guess.count(str(x)) for x in range(10)]
        
    correct = 0
    index = 0
        
    while index <= 9:
        if nfreq[index] < gfreq[index]:
            correct += nfreq[index]
        else:
            correct += gfreq[index]
        index += 1
            
    guesses.append([attempts, guess, correct])
        
    correct = 0
    index = 0
        
    while index <= 4:
        if number[index] == guess[index]:
            correct += 1
        index += 1
        
    guesses[-1].append(correct)
        
    print('\n'*50)
    header = ['Attempt', 'Guess', 'Correct Digits', 'Correctly Placed']
    eline = '='*52

    print(eline)
    for x in header:
        print('||'+x,end='')
    print('||')

    for x in [list(zip(y, header)) for y in guesses]:
        for a in x:
            z = (str(a[0]), a[1])
            spaces = ' '*int((len(z[1])-len(z[0]))/2)
            print('||'+spaces+z[0]+spaces,end='')
            if (len(z[1])-len(z[0]))%2 == 1:
                print(' ',end='')
        print('||')
    print(eline+'\n')
    
    if ''.join(number) == guess:
        print('====================\nCorrect! \n'+str(attempts)+' attempts.')
        t = time()-start
        print('Time: '+str(int(t//60))+':'+str(round(t%60, 2)))
        print(''.join(number))
        print('====================')
    else:
        compare()
        
compare()
'''
====================================================
||Attempt||Guess||Correct Digits||Correctly Placed||
||   1   ||11111||      1       ||       1        ||
||   2   ||22222||      0       ||       0        ||
||   3   ||33333||      0       ||       0        ||
||   4   ||44444||      2       ||       2        ||
||   5   ||55555||      0       ||       0        ||
||   6   ||66666||      1       ||       1        ||
||   7   ||77777||      1       ||       1        ||
||   8   ||14467||      5       ||       3        ||
||   9   ||14422||      3       ||       3        ||
||  10   ||14476||      5       ||       5        ||
====================================================

====================
Correct! 
10 attempts.
Time: 0:37.62
14476
====================

====================================================
||Attempt||Guess||Correct Digits||Correctly Placed||
||   1   ||11111||      2       ||       2        ||
||   2   ||22222||      0       ||       0        ||
||   3   ||33333||      0       ||       0        ||
||   4   ||44444||      0       ||       0        ||
||   5   ||55555||      0       ||       0        ||
||   6   ||66666||      1       ||       1        ||
||   7   ||77777||      2       ||       2        ||
||   8   ||11677||      5       ||       2        ||
||   9   ||11222||      2       ||       1        ||
||  10   ||12222||      1       ||       0        ||
||  11   ||22277||      2       ||       1        ||
||  12   ||22227||      1       ||       1        ||
||  13   ||61717||      5       ||       2        ||
||  14   ||71167||      5       ||       5        ||
====================================================

====================
Correct! 
14 attempts.
Time: 1:10.43
71167
====================
'''