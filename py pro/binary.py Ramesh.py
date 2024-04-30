def BinarySearch(array,low,high,key):
    mid=int ((low + high)//2)
    if high<low:
        return-1
    if array[mid]<key:
        return BinarySearch (array,mid+1,high,key)
    elif array[mid]>key:
        return BinarySearch(array,low,mid-1,key)
    else:
        return mid
    
arr=[1,2,3,4,5,6,7,8,9,10]

low=0
high=len(arr)-1
key=3
pos=BinarySearch(arr,low,high,key)
if pos == -1:
    print("The element is not present  in the array")
else:
    print("The elements is found at",pos)