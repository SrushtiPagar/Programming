Addition = lambda No1 , No2: No1 + No2

Subtraction= lambda No1, No2 : No1 - No2

print("Enter First Number : ")
Value1 = int(input())

print("Enter second Number : ")
Value2 = int(input())

Ret = Addition(Value1,Value2)
print("Addition is : ",Ret)

Ret = Subtraction(Value1,Value2)
print("Subtraction is : ",Ret)