def main():
    try :
        fobj = open("Demo.txt","a")
        print("file gets opened")

        fobj.write(" Pune Maharashtra")
        
        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not Present in Current Directory")

if(__name__ == "__main__"):
    main()