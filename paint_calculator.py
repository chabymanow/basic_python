import math


print("Paint calculator")

def calculate(width, height, cover):
    paint = math.ceil((width * height) / cover)
    return paint

width = int(input("Type the width of the wall:"))
height = int(input("Type the height of the wall:"))
cover = int(input("How many square meter the paint can cover:"))


print(calculate(width = width, height = height, cover = cover))