i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Done")

i = 1
while i <= 5:
    print("&" * i)
    i = i + 1
print("Done")

loop = True

while loop:
    name = input("insert something ")
    if name == "stop":
        break

while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')