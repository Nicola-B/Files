#Nicola Batty
#17/02/2015
#Files Revision Exercise 2

with open ("test data file.txt",mode="r",encoding="utf-8") as test_data:
    for line in test_data:
        print(line,end="")
