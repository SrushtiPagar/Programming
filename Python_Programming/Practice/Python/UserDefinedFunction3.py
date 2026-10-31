# Accept :one parameter
# Return :one value

def Marvellous(Value) :                      #user defined Function
    print("Inside Marvellous : ",Value)
    return 21

def main() :
    Ret = Marvellous(11)
    print("Return Value is : ",Ret)

if(__name__ == "__main__"):
    main()