def rotateleft(A,n,d):
    p=1
    
    while p<=d:
        last=A[0]
        for i in range(n-1):
            A[i]=A[i+1]
        A[n-1]=last
        p+=1
        
    return A

n=int(input("enter the array size"))
A=[]
for i in range(n):
    x=int(input())
    A.append(x)
d=int(input("enter the d value"))
print(rotateleft(A,n,d))