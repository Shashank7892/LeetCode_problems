#inbuilt_function

def rev(A):
    lst=A[::-1]
    return lst
n=int(input("enter the array size"))
A=[]
for i in range(n):
    x=input()
    A.append(x)
print(rev(A))