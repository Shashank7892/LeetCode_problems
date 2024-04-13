# Find the largest three distinct elements in an array
# Last Updated : 07 Mar, 2024
# Given an array with all distinct elements, find the largest three elements.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1). 

# Examples :

# Input: arr[] = {10, 4, 3, 50, 23, 90}
# Output: 90, 50, 23

def largest3(A):
    F=S=T=0
    for i in range(len(A)):
        if A[i]>F:
            T=S
            S=F
            F=A[i]
        elif A[i] > S and A[i]!=F:
            T=S
            S=A[i]
        elif A[i] > T and A[i]!=S and A[i]!=F:
            T=A[i]
    print(F,S,T)
n=int(input("enter the array size"))
A=[]
for i in range(n):
    x=int(input())
    A.append(x)
print(largest3(A))