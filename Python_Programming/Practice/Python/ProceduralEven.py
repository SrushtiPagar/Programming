def CheckEven(No):
    if(No % 2 == 0):
        print("It is a Even Number")
    else:
        print("Its Odd Number")


def main():
    Value = int(input("Enter Number: "))            #dual task Execution function (input)

    CheckEven(Value)

if(__name__ == "__main__"):
    main()