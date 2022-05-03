# .strip(), len(), .lower(), .upper(), .split()

#text = input("input something: ")
#print(text.strip())
#.strip() removes all the spaces before and after the word
#print(text)
#print(len(text))
#len() returns the length of a list or string
#print(text.lower())
#.split() actually uses a delimiter and seperates it from the string
#print(text.split("."))
#print(text.split())

#.find() and .count()

#string_1 = "hello"
#rint(string_1.find("l"))
#print(string_1.find("o"))
#string_2 = "heahskfsfeuahfksjdahskf"
#print(string_2.count("f"))
#print(string_2.count("a"))
string = input("type something ")
if string.count("_") > 0:
    print("not good")
else:
    print("good")

