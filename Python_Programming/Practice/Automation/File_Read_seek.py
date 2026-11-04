# seek(kuthe,kuthun)
# kuthun : 0/1/2

# 0 : starting
# 1 : Current
# 2 : End

def main():
    try :
        fobj = open("Demo.txt","r")
        print("file gets opened")

        fobj.seek(10,0)

        Data = fobj.read()

        print(Data)
        
        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not Present in Current Directory")

if(__name__ == "__main__"):
    main()