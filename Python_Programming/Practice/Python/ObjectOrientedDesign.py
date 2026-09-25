class Arithmetic:
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B
        
    #instance method cause it has self in its parameter
    def Addition(self):
        Ans = self.No1 + self.No2
        return Ans

    def Subtraction(self):
        Ans = self.No1 - self.No2
        return Ans

print("Enter First Number : ")
Value1 = int(input())

print("Enter second Number : ")
Value2 = int(input())

Aobj = Arithmetic(Value1,Value2)

#internally 
# #Ret = Addition(Aobj , Value1,Value2)
Ret = Aobj.Addition()          
print("Addition is : ",Ret)

Ret = Aobj.Subtraction()       
print("Subtraction is : ",Ret)