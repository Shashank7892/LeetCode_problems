# using while loop in java using temp variable and incrementing the start and decrementing the end ponters
#in python using swap method and incrementing

def reversedarray(A,start,end):
    while start<=end:
        A[start],A[end]=A[end],A[start]
        start+=1
        end-=1
    return A

n=int(input("enter the array size"))
A=[]
for i in range(n):
    x=input()
    A.append(x)
s=0
end=n-1
print(reversedarray(A,s,end))