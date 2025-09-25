import random

secret_number = random.randint(1,10)
print(secret_number)

guess_count = 0
guess = 0

while guess != secret_number:
    if guess_count == 0:
        guess = int(input('Enter guess number (1 to 10): '))
    else:
        print('Your guess was wrong. Try again')
        guess = int(input('Enter guess number (1 to 10): '))
    guess_count += 1
print(f"You guessed it in {guess_count} tries!")