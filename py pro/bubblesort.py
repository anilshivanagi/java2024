def bubblesort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
x=[37,45,6,78,45,56,78,98,34]
print("before sorting:",x)
bubblesort(x)
print("after sorting:",x)