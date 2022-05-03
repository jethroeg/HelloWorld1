name = input("type your name: ")
print("Welcome to this adventure", name)

answer = input("""You are on a dirt road, it has come to an end. choose between the two: 
left or right?
""").lower()

if answer == "left":
    answer = input("""You come across a river. Ycu can walk around it or swim. Choose between the two: 
(walk/swim)?
""").lower()

    if answer == "swim":
        print("You were eaten by a crocodile")

    elif answer == "walk":
        print("You tripped over a rock, fell down the river, and got eaten by a crocodile.")
    else:
        print("Not valid. You died.")

elif answer == "right":
    answer = input("""You come to a wobbly bridge. Choose between the two: 
(continue/go back)?
""").lower()
    if answer == "continue":
        print("the bridge collapsed. You died")

    elif answer == "go back":
        answer = input("""You walked for miles and saw a boar trap. 
(jump/go back)
""").lower()
        if answer == "jump":
            print("You died. Your body became a fertilizer. You cannot waste any valuable oxygen in this planet anymore. You WIN.")
        elif answer == "go back":
            print("You walked for months and died.")
        else:
            print("Not a valid option. You died")
    else:
        print("Not valid. You died.")

else:
    print("Not a valid option. You died")

print("thank you for trying", name)


