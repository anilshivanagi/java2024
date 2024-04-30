n=int(input("Enter the number terms:"))
a = 0
b = 1
c= 0

for x in range(n):
    print(c,end=" ")
    c = a+b
    b = a
    a= c