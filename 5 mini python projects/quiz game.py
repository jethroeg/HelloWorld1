print("welcome to my quiz")

playing = input("do you want to play? ")

if playing.lower() != "yes":
    quit()
print("okay let's play :)")
score = 0
answer = input("What does cpu stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does gpu stand for? ")

if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does ram stand for? ")

if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does psu stand for? ")

if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#print("You got " + str(score) + " questions correct!")
#print("You got " + str((score/4) * 100) + "%")
#print("You got " + str(score) + " question correct!")

if score == 1:
    print("You got", score, "question correct!")
else:
    print("You got " + str(score) + " questions correct!")

print("You got " + str((score/4) * 100) + "%")

