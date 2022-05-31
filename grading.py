students = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# more = ""
# while more != "n":
#     name = input("type the student`s name: ")
#     score = int(input("Score:"))

#     students[name] = score
#     more = input("More?: (y/n)")

for student in students.keys():
    grade = students[student]
    if grade >90 and grade <=100:
        print(student +" : Outstanding")
    if grade >80 and grade <=90:
        print(student +" : Exceeds Expectation")
    if grade >70 and grade <=80:
        print(student +" : Accepteble")
    if grade < 70:
        print(student +" : Fail")