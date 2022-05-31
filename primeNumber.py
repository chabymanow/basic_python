number = int(input("Give me number:"))

if number % 2 != 0 and number % 3 != 0 and number % 5 != 0:
    print("Your number is prime")
else:
    print("This number is not prime")