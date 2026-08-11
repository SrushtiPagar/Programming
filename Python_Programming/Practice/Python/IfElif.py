#print("-"*40)
print("------------------------------------------------")
print("------------Ticket Pricing Software-------------")
print("------------------------------------------------")

print("Please enter your age : ")
Age = int(input())

if(Age <= 5):
    print("FREE Entry")
elif(Age > 5 and Age <= 18):
    print("Ticket Price : 900")
elif(Age > 18 and Age <= 40):
    print("Ticket Price : 1200")
else:
    print("Ticket Price : 500")