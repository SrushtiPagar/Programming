def main():
    Ans = 0

    try : 
        print("Enter First Number : ")
        No1 = int(input())

        print("Enter Second Number : ")
        No2 = int(input())

        Ans = No1 / No2

        print("Division is Successful")                 #this line gets skips when exception occurs
        
    except ZeroDivisionError as zobj:                   #as - alies (nick name) 
        print("Exception Occur due to 2nd operant is 0",zobj)
    
    print("Result is : ",Ans)

if(__name__ == "__main__"):
    main()