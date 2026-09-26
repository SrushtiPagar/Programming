#Accessing class Variable

class Demo:
    #class variables
    Value1 = 10
    Value2 = 20

    def __init__(self):
        self.No1 = 11
        self.No2 = 21

    # Instance Method
    def fun(self):
        print("Inside instance method named as fun")
        print(self.No1)
        print(self.No2)
        #printing class variables using class name
        #this is good approach
        print(Demo.Value1)
        print(Demo.Value2)

#object creation
dobj = Demo()
dobj.fun()