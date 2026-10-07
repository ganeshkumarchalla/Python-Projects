print("Hello, welcome to the Pizza World!")

size = input("Which size of pizza would you like? S, M, or L: ").upper()
pepperoni = input("Do you want pepperoni? Type Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Type Y or N: ").upper()

bill = 0

# Base price
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid size selected.")

# Pepperoni cost
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:  # M or L
        bill += 3

# Extra cheese cost
if extra_cheese == "Y":
    bill += 2

print(f"Your final bill is ${bill}")
