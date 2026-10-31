# Accept :Multiple parameter
# Return :Multiple value

def Marvellous(Value1,Value2) :                      #user defined Function
    print("Inside Marvellous : ",Value1,Value2)
    return 21,51

def main() :
    Ret1,Ret2 = Marvellous(10,20)
    print("Return Values are : ",Ret1,Ret2)

if(__name__ == "__main__"):
    main()