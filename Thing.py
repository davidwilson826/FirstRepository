from random import randint

number = [str(randint(0,9)) for x in range(5)]
print(number)

guess = input("Guess a five digit number. ")
print(guess)

correct = 0

for x in guess:
    if guess.count(x) < number.count(x):
        correct += guess.count(x)
    else:
        correct += number.count(x)
        
print(correct)