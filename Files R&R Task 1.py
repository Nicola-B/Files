#Nicola Batty
#04/02/2015
#Files R&R Task 1

with open("students.txt", mode="r", encoding="utf-8") as students:
    for name in students:
        print(name)
