#hybrid

CheckEven = lambda No: (No % 2 == 0)                #Functional

def main():                                         #procedural
    Value = int(input("Enter Number: "))            #dual task Execution function (input)

    Ret = CheckEven(Value)                          #ret = (Value % 2 == 0)

    if(Ret == True):
        print("Number is Even")
    else:
        print("Number is Odd")
    

if(__name__ == "__main__"):
    main()