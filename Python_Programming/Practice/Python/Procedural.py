def Addition(No1 , No2):
    Ans = No1 + No2
    return Ans

def Subtraction(No1, No2):
    Ans = No1 - No2
    return Ans

print("Enter First Number : ")
Value1 = int(input())

print("Enter second Number : ")
Value2 = int(input())

Ret = Addition(Value1,Value2)
print("Addition is : ",Ret)

Ret = Subtraction(Value1,Value2)
print("Subtraction is : ",Ret)

#Also
# def main():
#     Value1 = int(input("Enter First Number : "))
#     Value2 = int(input("Enter Second Number : "))

# if(__name__ == "__main__"):
#     main()