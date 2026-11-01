import os
import sys
import hashlib

def CaculateChecksum(FileName):
    fobj = open(FileName,"rb")
    hobj = hashlib.md5()

    Buffer = hobj.read(1024)

    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer = hobj.read(1024)
    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryName):
    Ret = False

    Ret = os.path.exists(DirectoryName)

    if Ret == False:
        print("Path is Invalid")
        return

    Ret = os.path.isdir(DirectoryName)

    if Ret == False:
        print("It is not a directory")
        return

    Duplicate = {}

    Unique = 0
    Same = 0

    for FolderName , SubFolder , FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)

            Checksum =CaculateChecksum(fname)

            if Checksum in Duplicate:
                Duplicate(Checksum.append)
            else:
                Duplicate

def DeleteDuplicate(DirectoryName):
    myDict = FindDuplicate(DirectoryName)

    Result = list(filter(lambda x : len(x)>1, myDict.values()))

    Count = 0
    TotalDeleted = 0

    for value in Result:
        
        for subvalue in value:
            Count = Count+1
            if(Count>1):
                print("Duplicate found : ",subvalue)
                TotalDeleted = TotalDeleted + 1
        Count=0

    print("TotalDeleted files : ",TotalDeleted)

def main():
    Data = FindDuplicate("test")

if(__name__ == "__main__"):
    main()