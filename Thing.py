from random import randint

eline = '====================\n'

print(eline+
      '||Attempt||Guess||Correct Digits||Correctly Placed||')

#success = False
#number = [str(randint(0,9)) for x in range(5)]
number = '55890'
#print(number)

#global attempts
attempts = 0
#guesses = []

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
            
        #guesses.append([guess, correct])
                
        #print(str(correct)+' digits correct')
        
        cplc = 0
        index = 0
        
        while index <= 4:
            if number[index] == guess[index]:
                cplc += 1
            index += 1
            
        #print(str(cplc)+' digits correctly placed')
        
        print('||'+str(attempts)+'||'+guess+'||'+str(correct)+'||'+str(cplc)+'||')
        
        #guesses[-1].append(correct)
        
        #print(guesses)
        #print('\n'*50)
        #for x in guesses:
        #    
        #          eline+
        #          '||'+str(guesses.index(x)+1)+'||'+str(x[0])+'||'+str(x[1])+'||'+str(x[2])+'||\n'+
        #          eline)
        
        compare()
        
compare()