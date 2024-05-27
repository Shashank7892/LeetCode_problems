#User function Template for python3
class Solution:

	def maxSortedAdjacentDiff(self,arr, n):
	    maxdiff=0
	    if n<2:
            return 0
        else:
            arr.sort()
            for i in range(n-1):
                maxdiff=max(maxdiff,arr[i+1]-arr[i])
            return maxdiff
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
	
	tc=int(input())
	while tc > 0:
	    n=int(input())
	    a=list(map(int , input().strip().split()))
	    ob = Solution()
	    ans=ob.maxSortedAdjacentDiff(a, n)
	    print(ans)
	    tc=tc-1
# } Driver Code Ends