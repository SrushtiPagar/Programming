import threading

def Display():                                          #child thread
    print("Inside Display : ",threading.get_ident())

def main():                                             #parent thread
    print("Inside main : ",threading.get_ident())

    tobj = threading.Thread(target= Display)
                            #keyword argument

    tobj.start()

if(__name__ == "__main__"):
    main()