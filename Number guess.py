import random

number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == number:
        print("🎉 Correct! You won.")
        break
    elif guess > number:
        print("Too high!")
    else:
        print("Too low!")
