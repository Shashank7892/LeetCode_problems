# arr=[1,2,3,4,5,6,7]
# d=2
# o/p:[6,7,1,2,3,4,5]

def rotateright(A,d,n):
    lst=[]
    print(n-d)
    for i in range(n-d,n):
        lst.append(A[i])
        
    for j in range(n-d):
        lst.append(A[j])
    return lst

n=int(input("enter the array size"))
A=[]
for i in range(n):
    x=int(input())
    A.append(x)
d=int(input("enter the d value"))
print(rotateright(A,d,n))
