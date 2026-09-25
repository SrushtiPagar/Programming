class Arithmetic:
    def Addition(self,No1 , No2):
        Ans = No1 + No2
        return Ans

    def Subtraction(self,No1, No2):
        Ans = No1 - No2
        return Ans
    
Aobj = Arithmetic()

print("Enter First Number : ")
Value1 = int(input())

print("Enter second Number : ")
Value2 = int(input())

#internally 
# #Ret = Addition(Aobj , Value1,Value2)
Ret = Aobj.Addition(Value1,Value2)          
print("Addition is : ",Ret)

Ret = Aobj.Subtraction(Value1,Value2)       
print("Subtraction is : ",Ret)