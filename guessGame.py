secret = 37
attempts = 0

while True:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess > secret:
        print("Too High")

    elif guess < secret:
        print("Too Low")

    else:
        print("Correct!")
        print("Attempts:", attempts)
        break