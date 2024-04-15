# Count the elements
# EasyAccuracy: 25.32%Submissions: 38K+Points: 2
# Given two arrays a and b both of size n. Given q queries in an arrray query each having a positive integer x denoting an index of the array a. For each query, your task is to find all the elements less than or equal to a[x] in the array b.

# Example 1:

# Input:
# n = 3
# a[] = {4,1,2}
# b[] = {1,7,3}
# q = 2
# query[] = {0,1}
# Output : 
# 2
# 1
# Explanation: 
# For 1st query, the given index is 0, a[0] = 4. There are 2 elements(1 and 3) which are less than or equal to 4.
# For 2nd query, the given index is 1, a[1] = 1. There exists only 1 element(1) which is less than or equal to 1.


class Solution:
    def countElements(self, a, b, n, query, q):
        ans=[]
        
        for i in query:
            c=0
            for j in range(n):
                if a[i]>=b[j]:
                    c+=1
            ans.append(c)
        return ans
    
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    q=int(input())
    query=[]
    ob=Solution()
    for i in range(q):
        query.append(int(input()))
    ans=ob.countElements(a,b,n,query,q)
    for i in range(q):
        print(ans[i])