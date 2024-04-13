#using 2 array

def reversearray(A,s):
    # lst=[0]*s
    # for i in range(0,s):
    #     lst[i]=A[s-i-1]
    #return lst
    
# The error in the code lies in the reversearray function.lst=[] has no indices because there are no value and its a empty list
# In Python, you can't assign values to indices of an empty list using indexing like lst[i] = A[s-i-1] 
# because initially, the list lst has no elements, and you're trying to assign values to indices that don't exist. 
# Instead, you can use the append() method to add elements to the list. 
# Here's the corrected version of the reversearray function:
    lst=[]
    for i in range(s):
        lst.append(A[s-i-1])
    return lst

n=int(input("enter the array size"))
A=[]
for i in range(n):
    x=input()
    A.append(x)
print(reversearray(A,n))