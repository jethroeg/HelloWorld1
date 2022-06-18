import random, sys

print("ROCK, PAPER, SCISSORS")
wins = 0
losses = 0
ties = 0

#main loop asking for the player's response

while True:
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    pick = input()
    if pick == q:
        sys.exit()
    elif pick == "r" or pick == "p" or pick == "s":
        break
    print('type r, p, s, or q')

#player pick

if pick == "r":
    print("ROCK VERSUS")
elif pick == "p":
    print("PAPER VERSUS")
elif pick == "s":
    print("SCISSORS VERSUS")

#display what the computer chose

randomNumber = random.radint(1,4)

if randomNumber == 1:
    print("PAPER")
elif randomNumber == 2:
    print("ROCK")
elif randomNumber == 3:
    print("SCISSORS")

# Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties += 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins += 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins += 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins += 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses += 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses += 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses += 1



