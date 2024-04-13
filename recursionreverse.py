#using recursion

def recurreversed(A,start,end):
    if start>=end:
        return A
    A[start],A[end]=A[end],A[start]
    recurreversed(A,start+1,end-1)
    
n=int(input("enter the array size"))
A=[]
for i in range(n):
    x=input()
    A.append(x)
s=0
end=n-1
# print(recurreversed(A,s,end))

# The error in the code lies in the usage of the print statement. The recurreversed function doesn't return any value explicitly; 
# it modifies the list A in place by reversing its elements recursively. 
# Therefore, when you call print(recurreversed(A, s, end)), it prints None,
# which is the return value of the function since there is no explicit return statement for the base case.

# To fix this, you can directly call the recurreversed function without print and
# then print the modified list A after the function call. Here's the corrected version:
recurreversed(A,s,end)
print(A)