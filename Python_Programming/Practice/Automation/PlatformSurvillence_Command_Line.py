# python ProcessSurvillence.py 2 MarvellousLog
# python ProcessSurvillence.py time_travel Folder_Name
#                 0                 1           2
# len(sys.argv)-> 3

# python ProcessSurvillence.py --h
# python ProcessSurvillence.py --u
#                   0            1
# len(sys.argv)-> 2

import psutil       #module psutil
import sys
import os

def main():
    Border = "-"*50
    print(Border)
    print("------Marvellous PlatForm Survillence System------")
    print(Border)

    # --h & --u handling

    if(len(sys.argv)==2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation Script is used to perform ")
            print("1 : It fetch the information of running processes")
            print("2 : It fetch information about the primary storage as RAM")
            print("3 : It fetch information about the secondary storage as HDD")
            print("4 : It fetch the information about the microprocessor")
            print("6 : It maintains all records into log file")
            print("7 : It sendws the log file through mail periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the Automation Script as : ")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time Interval : Time in minutes for priodic execution")
            print("Folder_Name : Name of folder for the log file creation")

        else:
            print("Unable to proceed as is no matching arguments")
            print("Please use --h and --u flag for getting more details")
        

    #Actual Project code
    elif(len(sys.argv)==3):
        pass

    else:
        print("Invalid Number of Arguments")
        print("Unable to proceed as arguments are not matching")        
        print("Please use --h and --u flag for getting more details")


    print(Border)
    print("Thank you for using our Automation System")
    print(Border)
    

if(__name__ == "__main__"):
    main()


# C:\Users\Srushti Nitin Pagar\Desktop\Python\Automations>python ProcessSurvillence.py --u
# --------------------------------------------------
# ------Marvellous PlatForm Survillence System------
# --------------------------------------------------
# Use the Automation Script as :
# python ProcessSurvillence.py Time_Interval Folder_Name
# Time Interval : Time in minutes for priodic execution
# Folder_Name : Name of folder for the log file creation
# --------------------------------------------------
# Thank you for using our Automation System
# --------------------------------------------------

# C:\Users\Srushti Nitin Pagar\Desktop\Python\Automations>python ProcessSurvillence.py --h
# --------------------------------------------------
# ------Marvellous PlatForm Survillence System------
# --------------------------------------------------
# This Automation Script is used to perform
# 1 : It fetch the information of running processes
# 2 : It fetch information about the primary storage as RAM
# 3 : It fetch information about the secondary storage as HDD
# 4 : It fetch the information about the microprocessor
# 6 : It maintains all records into log file
# 7 : It sendws the log file through mail periodically
# --------------------------------------------------
# Thank you for using our Automation System
# --------------------------------------------------

# C:\Users\Srushti Nitin Pagar\Desktop\Python\Automations>python ProcessSurvillence.py -h
# --------------------------------------------------
# ------Marvellous PlatForm Survillence System------
# --------------------------------------------------
# Unable to proceed as is no matching arguments
# Please use --h and --u flag for getting more details
# --------------------------------------------------
# Thank you for using our Automation System
# --------------------------------------------------