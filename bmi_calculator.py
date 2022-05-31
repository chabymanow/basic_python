myheight = int(input("Your height: "))
myweight = int(input("Your weight: "))
myheight = myheight / 100
bmi = myweight / (myheight ** myheight)

print(bmi)