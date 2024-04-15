# Move all zeroes to end of array
# Last Updated : 18 Sep, 2023
# Given an array of random numbers, Push all the zero’s of a given array to the end of the array. For example, if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}. The order of all other elements should be same. Expected time complexity is O(n) and extra space is O(1).

# Example: 

# Input :  arr[] = {1, 2, 0, 4, 3, 0, 5, 0};
# Output : arr[] = {1, 2, 4, 3, 5, 0, 0, 0};

# Input : arr[]  = {1, 2, 0, 0, 0, 3, 6};
# Output : arr[] = {1, 2, 3, 6, 0, 0, 0};

def movezeroright(A,n):
    count=0
    
    for i in  range(n):
        if A[i]!=0:
            A[count]=A[i]
            count+=1
            
    while count<n:
        A[count]=0
        count+=1
    return A
        
n=int(input("enter the array size"))
A=[]
for i in range(n):
    x=int(input())
    A.append(x)
print(movezeroright(A,n))