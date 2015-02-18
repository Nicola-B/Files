#Nicola Batty
#17/02/2015
#Files Development Exercise 2

#import pdb
import pickle

class name_record:
    def __init__(self):
        self.name = None
        self.dofb = None

#pdb.set_trace()

name_list = []

end = False
while not end:
    name_dofb = name_record()
    name = input("Please enter a name(prese enter to end): ")
    if name != "":
        name_dofb.name = name
        name_dofb.dofb = input("Please enter there date of birth: ")
        name_list.append(name_dofb)
    else:
        end = True

with open("name records.dat",mode="wb") as name_file:
    pickle.dump(name_list,name_file)
