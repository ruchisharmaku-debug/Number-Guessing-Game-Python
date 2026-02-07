import random

secret_number = random.randint(1, 50)
attempts = 0

print("Welcome to the Number Guessing Game!")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too big!")
        else:
            print("You guessed it right!")
            print("Attempts:", attempts)
            break

    except:
        print("Please enter only numbers!")