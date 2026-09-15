no = 11                             #Global Variable

def Display():
    global no                       #exteren keyword
    no = 21
    print("From Display : ",no)     

print("Before : ",no)
Display()
print("After :",no)