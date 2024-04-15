def rotate(A,n,d):
    d=d%n # d=d%n provide the same value d
    
    lst=[]
    
    for i in range(d,n):
        lst.append(A[i])
    
    for j in range(d):
        lst.append(A[j])
    
    return lst

n=int(input("enter the array size"))
A=[]
for i in range(n):
    x=int(input())
    A.append(x)
d=int(input("enter the d value"))
print(rotate(A,n,d))