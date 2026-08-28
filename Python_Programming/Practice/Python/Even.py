# print("Enter a Number : ")
# No = int(input())

# if(No % 2 == 0 ) :
#     print("Number is Even")
# else :
#     print("Number is Odd")
# the Execution is start from the self executable line  which is at 0th indentation

def EvenOdd(No) : 
    if(No% 2 == 0) :
        print("Number is Even")
    else : 
        print("Number is odd")

def main() : 
    print("Enter the Number : ")
    No = int(input())
    EvenOdd(No)

if(__name__ == "__main__"):
    main()
    
