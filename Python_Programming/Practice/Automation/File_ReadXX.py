def main():
    try :
        fobj = open("Demo.txt","r")
        print("file gets opened")

        Data = fobj.read(10)

        print(Data)

        Data1 = fobj.read(14)

        print(Data1)
        
        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not Present in Current Directory")

if(__name__ == "__main__"):
    main()