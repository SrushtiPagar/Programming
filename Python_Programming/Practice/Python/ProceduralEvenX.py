def CheckEven(No):
    if(No % 2 == 0):
        return True
    else:
        return False


def main():
    Value = int(input("Enter Number: "))            #dual task Execution function (input)

    Ret = CheckEven(Value)

    if(Ret == True):
        print("Number is Even")
    else:
        print("Number Odd")
    

if(__name__ == "__main__"):
    main()