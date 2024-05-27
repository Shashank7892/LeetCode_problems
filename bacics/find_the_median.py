#User function Template for python3

class Solution:
	def find_median(self, v):
		v.sort()
		x=len(v)
		if len(v)%2!=0:
		    return v[(x-1)//2]
		else:
		    mid=(x-1)//2
		    res=(v[mid]+v[mid+1])//2
		    return res
		    
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split())) 
		ob = Solution()
		ans = ob.find_median(v)
		print(ans)
# } Driver Code Ends