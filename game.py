import random

secret_number = random.randint(1, 10)

print("🎮 Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 10")

attempts = 3

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("🎉 Correct! You win!")
        break

    else:
        attempts -= 1
        print("❌ Wrong guess!")

        if attempts > 0:
            print("Attempts left:", attempts)

if guess != secret_number:
    print("😢 You lost!")
    print("The correct number was:", secret_number)