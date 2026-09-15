no = 11                             #Global Variable

def Display():
    no = 21                     #local variable of Display
    #nearest no
    print("From Display : ",no)     

print("Before : ",no)
Display()
print("After :",no)