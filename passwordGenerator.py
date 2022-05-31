import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


pass_list = []
password = ""

nr_letters = int(input("How many letters do you want?: "))
nr_numbers = int(input("How many numbers do you want?: "))
nr_symbols = int(input("How many symbols do you want?: "))

for i in range(0, nr_letters):
    pass_list.append(random.choice(letters))

for i in range(0, nr_numbers):
    pass_list.append(random.choice(numbers))

for i in range(0, nr_symbols):
    pass_list.append(random.choice(symbols))

random.shuffle(pass_list)

for i in pass_list:
    password += i

print(password)