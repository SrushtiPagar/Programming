# 6 : 1 * 2 * 3 * 4 * 5 * 6
def Factorial(No):
    fact = 1
    
    for i in range(1,No+1):
        fact = fact * i

    return fact

def main():
    Value = int(input("Enter a Number : "))
    Ret = Factorial(Value)
    print("Factorial is : ",Ret)

if(__name__ == "__main__"):
    main()