from random import randint

#success = False
number = [str(randint(0,9)) for x in range(5)]#'55890'
#print(number)

global attempts
attempts = 0

#while success == False:

def compare():
    
    guess = input("Guess a five digit number. ")#'58995'
    #print(guess)
    
    attempts += 1
    
    if ''.join(number) == guess:
        print('===================='
            'Correct! '+str(attempts)+' attempts.'
            ''.join(number)
            '====================')
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
                
        print(str(correct)+' digits correct')
        
        correct = 0
        index = 0
        
        while index <= 4:
            if number[index] == guess[index]:
                correct += 1
            index += 1
            
        print(str(correct)+' digits correctly placed')
        
        compare()
        
compare()