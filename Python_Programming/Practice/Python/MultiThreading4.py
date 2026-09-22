import threading

def Display(No1,No2,No3):            #  def Display(*No)                                      #child thread
    print(f"Inside Display {No1,No2,No3} : ",threading.get_ident())

def main():                                             #parent thread
    print("Inside main : ",threading.get_ident())

    tobj = threading.Thread(target= Display,args=(11,21,51,))         #list of Values (this is constant cause it is tuple)
                            #keyword argument

    tobj.start()

if(__name__ == "__main__"):
    main()