from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
peopleList = {}
bids = []
morePeople = "y"

clear()
print(logo)

def getMax(dic):
     v = list(dic.values())
     k = list(dic.keys())
     return k[v.index(max(v))]

while morePeople == "y":
  name = input("Type your name: ")
  bid = int(input("Make a bid: "))
  peopleList.update({name: bid})
  morePeople = input("More people? (y/n)")
  clear()
  print(logo)

print(f" The winner of this auction is: {getMax(peopleList)}")