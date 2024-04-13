# Find Second largest element in an array
# Last Updated : 08 Apr, 2024
# Given an array of integers, our task is to write a program that efficiently finds the second-largest element present in the array. 

# Examples:

# Input: arr[] = {12, 35, 1, 10, 34, 1}
# Output: The second largest element is 34.
# Explanation: The largest element of the array is 35 and the second largest element is 34

# Input: arr[] = {10, 5, 10}
# Output: The second largest element is 5.
# Explanation: The largest element of the array is 10 and the second largest element is 5

def secondmax(A):
    maxi=A[0]
    secondmax=-1
    
    for i in range(1,len(A)):
        if A[i] > maxi:
            secondmax=maxi
            maxi=A[i]
        elif A[i] > secondmax and A[i]!=maxi:
            secondmax=A[i]
    return secondmax
            
n=int(input("enter the array size"))
A=[]
for i in range(n):
    x=int(input())
    A.append(x)
print(secondmax(A))