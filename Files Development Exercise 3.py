#Nicola Batty
#17/02/2015
#Files Development Exercise 3

import pickle

class name_record:
    def __init__(self):
        self.name = None
        self.dofb = None

with open("name records.dat",mode="rb") as name_file:
    names = pickle.load(name_file)

for name_dofb in names:
    print(name_dofb.name)
    print(name_dofb.dofb)
