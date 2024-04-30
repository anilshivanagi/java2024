import time
def linearsearch (arr,x):
    i=0
    while i<len (arr):
        if arr[i]==x:
            return i
        i=i+1
    return-1
arr=list()
start=time.time()
n=int(input("Enter the no of elements"))
for i in range (n):
    number=int(input("Enter the elements"))
    arr.append(number)
x=int(input("Enter the elements to be searched"))
r=linearsearch (arr,x)
if r>0:
    print("Elements is fond as ",r)
else:
    print("Element is not found")
    end=time.time()
    print("Time the execution" ,end- start)