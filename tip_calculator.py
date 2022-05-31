bill = int(input("How much the bill is?: "))
person = int(input("How many people are there?: "))
tip_amount = int(input("How much tip you want to pay?:"))
tip = bill *  (tip_amount / 100)
total_bill = bill + tip
result = total_bill / person
print("the amount of money par person: " + str(result))