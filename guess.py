import random
n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0
while guess != to_be_guessed:
    guess = int(input("new number: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number is too large")
        elif guess < to_be_guessed:
            print("Number is too small")
    else:
        print("sorry not correct")
        break
else:
    print("congratulation you made it")