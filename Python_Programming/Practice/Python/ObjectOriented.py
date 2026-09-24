class Arithmetic:
    def Addition(No1 , No2):
        Ans = No1 + No2
        return Ans

    def Subtraction(No1, No2):
        Ans = No1 - No2
        return Ans
    
Aobj = Arithmetic()

print("Enter First Number : ")
Value1 = int(input())

print("Enter second Number : ")
Value2 = int(input())

Ret = Aobj.Addition(Value1,Value2)          # Error
print("Addition is : ",Ret)

Ret = Aobj.Subtraction(Value1,Value2)       # Error
print("Subtraction is : ",Ret)