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
        if round(t%60, 2) < 10:
            placeholder = ':0'
        else:
            placeholder = ':'
        print('Time: '+str(int(t//60))+placeholder+str(round(t%60, 2)))
        print(''.join(number))
        print('====================')
    else:
        compare()
        
compare()
'''
Record Progression:

====================================================
||Attempt||Guess||Correct Digits||Correctly Placed||
||   1   ||11111||      0       ||       0        ||
||   2   ||22222||      0       ||       0        ||
||   3   ||33333||      2       ||       2        ||
||   4   ||44444||      0       ||       0        ||
||   5   ||55555||      0       ||       0        ||
||   6   ||66666||      3       ||       3        ||
||   7   ||33666||      5       ||       5        ||
====================================================

====================
Correct! 
7 attempts.
Time: 0:11.58
33666
====================

*

====================================================
||Attempt||Guess||Correct Digits||Correctly Placed||
||   1   ||11111||      0       ||       0        ||
||   2   ||22222||      1       ||       1        ||
||   3   ||33333||      0       ||       0        ||
||   4   ||44444||      0       ||       0        ||
||   5   ||55555||      0       ||       0        ||
||   6   ||66666||      1       ||       1        ||
||   7   ||77777||      1       ||       1        ||
||   8   ||88888||      1       ||       1        ||
||   9   ||99999||      0       ||       0        ||
||  10   ||26780||      5       ||       5        ||
====================================================

====================
Correct! 
10 attempts.
Time: 0:24.24
26780
====================

====================================================
||Attempt||Guess||Correct Digits||Correctly Placed||
||   1   ||11111||      0       ||       0        ||
||   2   ||22222||      1       ||       1        ||
||   3   ||33333||      1       ||       1        ||
||   4   ||44444||      1       ||       1        ||
||   5   ||55555||      0       ||       0        ||
||   6   ||66666||      1       ||       1        ||
||   7   ||77777||      0       ||       0        ||
||   8   ||88888||      0       ||       0        ||
||   9   ||99999||      1       ||       1        ||
||  10   ||23469||      5       ||       3        ||
||  11   ||23411||      3       ||       1        ||
||  12   ||21111||      1       ||       1        ||
||  13   ||24369||      5       ||       5        ||
====================================================

====================
Correct! 
13 attempts.
Time: 0:33.77
24369
====================

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

------------------------------------------------------

Honorary Mentions:

*
====================================================
||Attempt||Guess||Correct Digits||Correctly Placed||
||   1   ||11111||      0       ||       0        ||
||   2   ||22222||      0       ||       0        ||
||   3   ||33333||      0       ||       0        ||
||   4   ||44444||      2       ||       2        ||
||   5   ||55555||      0       ||       0        ||
||   6   ||66666||      0       ||       0        ||
||   7   ||77777||      0       ||       0        ||
||   8   ||88888||      0       ||       0        ||
||   9   ||99999||      1       ||       1        ||
||  10   ||44900||      5       ||       3        ||
||  11   ||44911||      3       ||       2        ||
||  12   ||44111||      2       ||       2        ||
||  13   ||44009||      5       ||       5        ||
====================================================

====================
Correct! 
13 attempts.
Time: 0:31.2
44009
====================

------------------------------------------------------

====================================================
||Attempt||Guess||Correct Digits||Correctly Placed||
||   1   ||11111||      1       ||       1        ||
||   2   ||22222||      0       ||       0        ||
||   3   ||33333||      1       ||       1        ||
||   4   ||44444||      1       ||       1        ||
||   5   ||55555||      1       ||       1        ||
||   6   ||66666||      0       ||       0        ||
||   7   ||77777||      1       ||       1        ||
||   8   ||13457||      5       ||       3        ||
||   9   ||13422||      3       ||       2        ||
||  10   ||13222||      2       ||       2        ||
||  11   ||13574||      5       ||       3        ||
||  12   ||13522||      3       ||       3        ||
||  13   ||13547||      5       ||       5        ||
====================================================

====================
Correct! 
13 attempts.
Time: 0:44.12
13547
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