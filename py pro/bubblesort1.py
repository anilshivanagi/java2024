import time
import numpy as np
import matplotlib.pyplot as plt
def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[i]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
times=list()
arr=list()
numtimes=list()
for i in range(1,9):
    start=time.time()
    n=int(input("Enter the no of elements"))
    numtimes.append(n)
    for x in range(n):
        number=np.random.randint(1,10)
        arr.append(n)
    print("List after bubblesort of",x+1,"elments")
    print(arr)
    bubblesort(arr)
    end=time.time()
    times.append(end-start)
    print("list after bubblesort of",x+1,"elements")
    print(arr)
    print("time taken for bubblesort for",n,"elements is",end-start)
print(numtimes)
print(times)
plt.xlabel("list length")
plt.ylabel("time complexity")
plt.plot(numtimes,times,label="bubblesort")
plt.grid()
plt.legend()
plt.show()