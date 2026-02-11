import random

def guessNumber(secerectNumber):
    
    for i in range(1,4):
        guessedNumber = int(input('Try to guess the number: '))
        if guessedNumber < secerectNumber:
            print('The number is too low')
        elif guessedNumber > secerectNumber:
            print("The number is too high")
        else:
            break;
    return guessedNumber



def check(guessedNumber, secerectNumber):
    if (gussedNumber == secerectNumber):
        print('Congrats! You gussed correct number!!')
    else:
        print('Better luck next time!')




secerectNumber = random.randint(1,10)
gussedNumber = guessNumber(secerectNumber)
check(gussedNumber, secerectNumber)
