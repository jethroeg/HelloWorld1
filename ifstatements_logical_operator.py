is_hot = True
is_cold = False

if is_hot:
    print("it's a hot day")
    print("drink plenty of water")
elif is_cold:
    print("it is cold")
    print("wear warm clothes")
else:
    print("it's a lovely day")
print("have a good day")

price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = .1 * price
else:
    down_payment = .2 * price
print(f"down_payment ${down_payment}")

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("eligible for loan")


has_high_income = True
has_criminal_record = False
if has_high_income and not has_criminal_record:
    print("eligible for loan")

# and = both is satisfied, or = at least one

temperature = 30
if temperature > 30:
    print("it's a hot day")
else:
    print("it's not a hot day")
# you can also use >= <= == != (not equal)

name = "j"

if len(name) < 3:
    print("name must be at least 3 characters ")
elif len(name) >50:
    print("name must be a maximum of 50 characters")
else:
    print("name looks good!")
