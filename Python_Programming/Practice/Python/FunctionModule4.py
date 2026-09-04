from Marvellous import Addition,Subtraction       

def main() :
    print("Enter First number : ")
    Value1 = int(input())

    print("Enter Second number : ")
    Value2 = int(input())

    Ret = Addition(Value1 , Value2)            
    print("Addition is : ",Ret)

    Ret = Subtraction(Value1 , Value2)          #Error
    print("Subtraction is : ",Ret)

if (__name__ == "__main__") :
    main()