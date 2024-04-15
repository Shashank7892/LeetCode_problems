def rotateright2(A,n,d):
    p=1
    
    while p <=d:
        first=A[n-1]
        for i in range(n-1,0,-1):
            A[i]=A[i-1]
        A[0]=first
        
        p+=1
        
    return A

n=int(input("enter the array size"))
A=[]
for i in range(n):
    x=int(input())
    A.append(x)
d=int(input("enter the d value"))
print(rotateright2(A,n,d))

            
