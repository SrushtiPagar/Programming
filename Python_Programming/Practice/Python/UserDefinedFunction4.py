# Accept :Multiple parameter
# Return :one value

def Marvellous(Value1,Value2) :                      #user defined Function
    print("Inside Marvellous : ",Value1,Value2)
    return 21

def main() :
    Ret = Marvellous(10,20)
    print("Return Value is : ",Ret)

if(__name__ == "__main__"):
    main()