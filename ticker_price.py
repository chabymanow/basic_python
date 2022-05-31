price = 0
height = int(input("What is your height in cm"))
if height>120:
    print("Go to ride")
    age = int(input("How many years old are you?"))
    if age < 12:
        price += 5
    if age > 12 and age < 18:
        price += 7
    if age > 18:
        price += 12
    photo = input("Would you like photo? (y/n)")
    if photo == "y":
        price += 3
    if photo == "n":
        price = price
    print("The final price is: " + str(price))
else:
    print("You not enough tall for this.")

