#Nicola Batty
#17/02/2015
#Files Development Exercise 4

import pickle

class name_record:
    def __init__(self):
        self.name = None
        self.dofb = None

with open("name records.dat",mode="rb") as name_file:
    names = pickle.load(name_file)



print("_"*31)
print("|{0:<15}|{1:>13}|".format("Name", "Date of birth"))
print("_"*31)
for name_dofb in names:
    print("|{0:<15}|{1:>13}|".format(name_dofb.name, name_dofb.dofb))
    print("_"*31)
