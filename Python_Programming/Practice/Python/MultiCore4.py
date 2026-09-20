import time
import os
import multiprocessing

def SumCube(No):
    print("Process is running with PID : ",os.getpid())
    
    Sum = 0
    for i in range(1,No+1):
        Sum = Sum+(i**3)

    return Sum

def main():
    Data = [10000000,20000000,30000000,40000000,50000000]

    Result = []

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()                   #pool - 

    #It applies the function to every item in the iterable.
    Result = pobj.map(SumCube,Data)                 #pobj- obj, map - allow method to execute 

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("Result is : ",Result)
    print(f"Time Required is : {end_time - start_time : .4f} seconds")

    

if(__name__ == "__main__"):
    main()