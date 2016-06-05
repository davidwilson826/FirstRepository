'''
3 attempts (really lucky)

9 attempts
8 attempts
'''

from random import randint

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
        print('====================\nCorrect! '+str(attempts)+' attempts.')
        print(''.join(number))
        print('====================')
    else:
        compare()
        
compare()