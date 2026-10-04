import time

def Factorial(No):
    fact = 1
    
    for i in range(1,No+1):
        fact = fact * i

    return fact

def main():
    Value = int(input("Enter a Number : "))

    start_time = time.perf_counter()

    Ret = Factorial(Value)

    end_time = time.perf_counter()

    print(f"Factorial is {Value} is : {Ret}")

    print(f"Time required is : {end_time - start_time: .5f} seconds")

if(__name__ == "__main__"):
    main()

    