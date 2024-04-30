def bs(arr,y,low,high):
    mid = ((high + low)//2)
    if high < low:
        return -1
    if arr[mid] == y:
        return mid
    elif arr[mid] < y:
        low = mid+1
        return bs(arr,y,low,high)
    else:
        high = mid -1
        return bs(arr,y,low,high)
    
arr = [12,13,15,17,18,20,22,24]

y =int(input("Enter a num:"))
low = 0
high = len(arr)-1
print(bs(arr,y,low,high))