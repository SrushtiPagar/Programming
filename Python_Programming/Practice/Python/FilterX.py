def CheckEven(No):
    return(No%2 == 0)

def main():
    Data = [13,12,8,10,11,20]

    print("Input Data is : ",Data)

    #function passed to filter should always return true or false
    #Iterable = filer(Iterable(list),Function)
    FData = list(filter(CheckEven,Data))

    print("Data After Filter : ",FData)

if(__name__ == "__main__"):
    main()