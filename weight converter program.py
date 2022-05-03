weight = int(input("weight: "))
unit = input("(L)bs or K(g): ")
if unit.upper() == "L":
    converted = weight / 2.2
    print(f"You are {converted} kilos")
else:
    converted = weight * 2.2
    print(f"You are {converted} lbs")