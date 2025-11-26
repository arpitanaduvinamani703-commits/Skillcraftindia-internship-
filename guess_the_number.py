import random

print("Guess the Number Game!")
number = random.randint(1, 100)

while True:
    guess = int(input("Enter your guess (1-100): "))

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! You guessed the number!")
        break
