import os

def main():
    ret = os.path.exists("Demo.txt")            #return true or false

    if(ret == True):
        print("File is present in Current Directory")
    else:
        print("There is no such file")

if(__name__ == "__main__"):
    main()