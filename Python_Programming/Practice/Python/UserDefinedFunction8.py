def BigBazar():
    print("Inside BigBazar")

    def Amul():
        print("Inside Amul Icecream parlour")

def main() :
    BigBazar()              #Allowed
    # Amul()                Name Error
    # BigBazar.Amul()       function' object has no attribute 'Amul

if(__name__ == "__main__"):
    main()