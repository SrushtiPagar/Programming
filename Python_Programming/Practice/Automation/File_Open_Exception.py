def main():
    try :
        open("Demo.txt","r")
        print("file gets opened")

    except FileNotFoundError as fobj:
        print("File is not Present in Current Directory")

if(__name__ == "__main__"):
    main()