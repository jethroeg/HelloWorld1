import random
secretNumber = random.radint(1,21)
print("I'm thinking of a number 1 to 20")

# Ask the player to guess 6 times.
for guessesTaken in range(1,7):
    print("Take a guess.")
    guess = int(input())

    if guess < secretNumber:
        print("pick higher")
    elif guess > secretNumber:
        print("pick lower")
    else:
        break

if guess == secretNumber:
    print("you got it in" + str(guessesTaken) + "tries")
else:
    print("Nope. the number i was thinking of was" + str(secretNumber))










