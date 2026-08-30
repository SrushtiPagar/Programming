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
        print("Exception Occured due to 2nd operant is 0",zobj)

    except ValueError as vobj:
        print("Exception Occured due to Invalid DataType",vobj)
    
    except Exception as eobj:                           #at least this exception should be written (this should be written at the bottom)
        print("Exception Occurred",eobj)                #this is generic exception
    
    finally : 
        print("Inside Finally Block")

    print("Result is : ",Ans)

if(__name__ == "__main__"):
    main()