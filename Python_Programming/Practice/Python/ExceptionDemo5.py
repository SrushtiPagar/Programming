def main():
    Ans = 0

    try : 
        print("Enter First Number : ")
        No1 = int(input())

        print("Enter Second Number : ")
        No2 = int(input())

        Ans = No1 / No2

        print("Division is Successful")                 #this line gets skips when exception occurs

    except Exception as eobj:                           #at least this exception should be written
        print("Exception Occurred",eobj)                #this is generic exception
    
    print("Result is : ",Ans)

if(__name__ == "__main__"):
    main()