import random, sys

print("ROCK, PAPER, SCISSORS")
wins = 0
losses = 0
ties = 0

while True:
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    pick = input()
    if pick == q:
        sys.exit()
    elif pick == "r" or pick == "p" or pick == "s":
        break
    print('type r, p, s, or q')

if pick == "r":
    print("ROCK VERSUS")
elif pick == "p":
    print("PAPER VERSUS")
elif pick == "s":
    print("SCISSORS VERSUS")

randomNumber = random.radint(1,4)

if randomNumber == 1:
    print("PAPER")
elif randomNumber == 2:
    print("ROCK")
elif randomNumber == 3:
    print("SCISSORS")

if
    #to be continued



