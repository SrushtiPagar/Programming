def main():
    try :
        fobj = open("Demo.txt","r")
        print("file gets opened")

        print("File offset is : ",fobj.tell())  #0

        Data = fobj.read(10)

        print(Data)

        print("File offset is : ",fobj.tell())

        Data = fobj.read(10)

        print(Data)

        print("File offset is : ",fobj.tell())
        
        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not Present in Current Directory")

if(__name__ == "__main__"):
    main()