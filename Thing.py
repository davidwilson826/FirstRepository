from random import randint

number = '55890'#[str(randint(0,9)) for x in range(5)]
print(number)

guess = '12355'#input("Guess a five digit number. ")
print(guess)

nfreq = [number.count(str(x)) for x in range(10)]
gfreq = [guess.count(str(x)) for x in range(10)]

correct = 0
index = 0

while index <= 10:
    if nfreq[index] < gfreq[index]:
        correct += nfreq[index]
    else:
        correct += gfreq[index]
        
print(correct)