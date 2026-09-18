CheckEven = lambda No: (No%2 == 0)
Increment = lambda No:  No+1
Addition = lambda No1,No2: No1 + No2

def filterX(Task , Elements):
    Result = []

    for no in Elements:
        Ret = Task(no)          #checkEven(no)
        if(Ret == True):
            Result.append(no)

    return Result

#-----------------------------------------------------------------

def mapX(Task , Elements):
    Result = []

    for no in Elements:
        Ret = Task(no)          # Increment(no)
        Result.append(Ret)

    return Result

#-------------------------------------------------------------------------

def reduceX(Task , Elements):
    Result = 0

    for no in Elements:
        Result = Task(Result,no)

    return Result

#-------------------------------------------------------------------------

def main():
    Data = [13,12,8,10,11,20]

    print("Input Data is : ",Data)

    FData = list(filterX(CheckEven,Data))
    print("Data After Filter : ",FData)

    MData = list(mapX(Increment,FData))
    print("Data After Map : ",MData)

    RData = reduceX(Addition,MData)

    print("Dagta After Reduce : ",RData)

if(__name__ == "__main__"):
    main()  