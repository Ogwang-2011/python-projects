import random

score = 10
random_number = random.randint(1, 10)

while True:
    try:
        user_input = int(input("Guess a number between 1 and 10: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if user_input == random_number:
        print(f"🎉 Congratulations! You guessed it right. Your score is {score}.")
        break
    else:
        print("❌ Better luck next time!")
        score -= 1
