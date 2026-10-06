print("Welcome to the roller coaster ride")
height = int(input("Enter your height: "))
bill = 0

if height >= 130:
    print("You can ride the roller coaster")
    age = int(input("Enter your age: "))

    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age >= 12 and age <= 18:
        bill = 7
        print("Teenage tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")

    want_photos = input("Do you want a photo? Type 'y' for yes: ")
    if want_photos == "y":
        bill += 3

    print(f"Please pay your total bill ${bill}")
else:
    print("Grow taller before you ride the roller coaster")