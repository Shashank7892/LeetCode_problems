def movezero(A,n):
    j=0
    for i in range(n):
        if A[i]!=0:
            A[i],A[j]=A[j],A[i]
            j+=1
    return A

n=int(input("enter the array size"))
A=[]
for i in range(n):
    x=int(input())
    A.append(x)
print(movezero(A,n))