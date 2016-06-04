from random import randint

#eline = '====================\n'

#success = False
#number = [str(randint(0,9)) for x in range(5)]
number = '55890'
#print(number)

#global attempts
attempts = 0
guesses = []

#while success == False:

def compare():
    
    guess = input("Guess a five digit number. ")#'58995'
    #print(guess)
    global attempts
    attempts += 1
    #print(attempts)
    if ''.join(number) == guess:
        print('====================\nCorrect! '+str(attempts)+' attempts.')
        print(''.join(number))
        print('====================')
#        print(''.join(number))
#        success = True
        
    else:
    
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
                
        print(str(correct)+' digits correct')
        
        correct = 0
        index = 0
        
        while index <= 4:
            if number[index] == guess[index]:
                correct += 1
            index += 1
            
        print(str(correct)+' digits correctly placed')
        
        guesses[-1].append(correct)
        
        #print(guesses)
        print('\n'*50)
        header = ['Attempt', 'Guess', 'Correct Digits', 'Correctly Placed']
        eline = '='*57
        #print(eline+
        #          '||Attempt||Guess||Correct Digits||Correctly Placed||')
        print(eline)
        for x in header:
            print('||'+x,end='')
        print('||')
        #for x in zip(guesses, [header for x in guesses]):
        #print([list(zip(y, header)) for y in guesses])
        for x in [list(zip(y, header)) for y in guesses]:
            for a in x:
                z = (str(a[0]), a[1])
                spaces = ' '*int((len(z[1])-len(z[0]))/2)
                print('||'+spaces+z[0]+spaces,end='')
                if (len(z[1])-len(z[0]))%2 == 1:
                    print(' ',end='')
            print('||')
        print(eline+'\n')
                    #eline+
                #  '||   '+str(x[0])+'   ||'+str(x[1])+'||'+str(x[2])+'||'+str(x[3])+'||')
        
        compare()
        
compare()