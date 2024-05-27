# Given a Integer array A[] of n elements. Your task is to complete the function PalinArray. 
# Which will return 1 if all the elements of the Array are palindrome otherwise it will return 0.

# Example 1:

# Input:
# 5
# 111 222 333 444 555

# Output:
# 1

# Explanation:
# A[0] = 111 //which is a palindrome number.
# A[1] = 222 //which is a palindrome number.
# A[2] = 333 //which is a palindrome number.
# A[3] = 444 //which is a palindrome number.
# A[4] = 555 //which is a palindrome number.
# As all numbers are palindrome so This will return 1.

# Your task is to complete this function
# Function should return True/False or 1/0
def PalinArray(arr ,n):
    c=0
    for i in arr:
        temp=i
        rev=0
        while i>0:
            dig=i%10
            rev=rev*10+dig
            i=i//10
        if rev==temp:
            c+=1
    
    if c==n:
        return 1
    else:
        return 0



#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr, n):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends