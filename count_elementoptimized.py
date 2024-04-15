class Solution:
    def countElements(self, a, b, n, query, q):
        # code here
        b.sort()
        ans=[]
        
        for i in query:
            left=0
            high=n-1
            while left<=high:
                mid=(left+high)//2
                if b[mid]<=a[i]:
                    left=mid+1
                else:
                    high=mid-1
            ans.append(left)
        return ans