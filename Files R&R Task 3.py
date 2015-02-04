#Nicola Batty
#04/02/2015
#Files R&R Task 3

with open("students.txt", mode="w", encoding="utf-8") as students:
        
    students.write("John")
    students.write("Isabella")

with open("students.txt", mode="r", encoding="utf-8") as students:
    for name in students:
        print(name)
