import random 

def guess(x):
    random_number = random.randint(1,x)
    guess = 0 
    while (guess != random_number):
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('too low')
        elif guess > random_number:
            print('too high')

    print(f'correct number: {random_number}')

def computer_guess(x):
    low = 1 
    high = x 
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        
        else:
            guess = low
        feedback = input(f'is {guess} too high (H), low (L) or correct (C)?').lower()
        if feedback == 'h':
            high = guess - 1 
        if feedback == 'l':
            low = guess + 1

    print(f'Computer guessed {guess} correctly.') 

computer_guess(10)

# guess(10)

