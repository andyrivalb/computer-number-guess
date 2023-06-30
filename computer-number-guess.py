import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input("Tebak angka yang benar: "))
        if guess > random_number:
            print(f'Sorry, {guess} too high!!')
        elif guess < random_number:
            print(f'Sorry, {guess} too low!')
    print(f'Yay, anda benar. {random_number} adalah angka yang benar!')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay, the computer have guessed the number {guess} correctly!')


computer_guess(100)