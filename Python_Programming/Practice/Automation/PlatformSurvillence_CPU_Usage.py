import psutil       #module psutil
import sys
import os
import time
import schedule

def PlatformSurvillence(FolderName):
    Border = "-"*50

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to proceed as directory name is existing but its not a directory")
            return
    else:
        os.mkdir(FolderName)        #make Directory
        print("Directory for the logfile gets created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)

    fobj = open(FileName,"w")

    print(f"Log File gets Succcessfully created with name {FileName}")

    fobj.write(Border+"\n")
    fobj.write("------Marvellous PlatForm Survillence System------\n")
    fobj.write("Log file gets created at : "+timestamp+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("----------------------------System Report-------------------\n")

    fobj.write("Number of active CPU cores : %s\n" %psutil.cpu_count())
    fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    fobj.write("\n\n\n\n\n\n\n\n\n\n\n")

    fobj.write(Border+"\n")
    fobj.write("-----------------------End of Log File-----------------------")
    fobj.write(Border+"\n")

    fobj.close()

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
        # print("CPU Usage : ",psutil.cpu_percent())
        print("Schedular started successfully")
        print("Press Ctrl + C to abort the automation script")

        schedule.every(int(sys.argv[1])).minute.do(PlatformSurvillence,sys.argv[2])

        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Number of Arguments")
        print("Unable to proceed as arguments are not matching")        
        print("Please use --h and --u flag for getting more details")


    print(Border)
    print("Thank you for using our Automation System")
    print(Border)
    

if(__name__ == "__main__"):
    main()
