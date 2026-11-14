def Display(*Data):                     #- *is n number of parameters
    print(Data)
    print(type(Data))

def main():
    Display(10,20.45,False,"Python")

if(__name__ == "__main__") :
    main()