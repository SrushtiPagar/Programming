import threading

def Display(No):            #  def Display(*No)                                      #child thread
    print(f"Inside Display {No} : ",threading.get_ident())

def main():                                             #parent thread
    print("Inside main : ",threading.get_ident())

    tobj = threading.Thread(target= Display,args=(11,))         #list of Values (this is constant cause it is tuple)
                            #keyword argument

    tobj.start()

if(__name__ == "__main__"):
    main()