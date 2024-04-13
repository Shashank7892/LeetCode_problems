# n=int(input("enter the array size"))
# lst=[]
# for i in range(n):
#     x=input()
#     lst.append(x)
# delet=input("enter the element to be deleted")
# pos=0
# for i in range(0,n):
#     if lst[i]==delet:
#         pos=i
#         break
# for i in range(pos,n-1):
#     lst[i]=lst[i+1]

# print(lst[0:n-1])

#using def function

def delete(A,n,x):
    ps=0
    for i in range(0,n):
        if A[i]==x:
            pos=i
            break
    for i in range(pos,n-1):
        A[i]=A[i+1]
    
    return n-1
    
n=int(input("enter the array size"))
lst=[]
for i in range(n):
    x=input()
    lst.append(x)
delet=input("enter the element to be deleted")
x=delete(lst,n,delet)
for i in range(x):
    print(lst[i],end=" ")