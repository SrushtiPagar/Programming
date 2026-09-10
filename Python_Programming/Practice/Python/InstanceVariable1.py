class Marvellous:
    #class variable
    No1 = 11
    No2 = 12

    def __init__(self):         #used to initialize instance variable
        #Instance Variable
        self.Value1 = 21
        self.Value2 = 51

print(Marvellous.No1)
print(Marvellous.No2)

#object / Instance Creation
mobj1 = Marvellous()
mobj2 = Marvellous()
mobj3 = Marvellous()

print(mobj1.Value1)
print(mobj2.Value1)