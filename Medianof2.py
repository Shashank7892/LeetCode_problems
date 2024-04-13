class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        li=nums1+nums2
        li.sort()
        n=len(li)
        if n%2==0:
            m1=li[n//2]
            m2=li[n//2-1]
            median=(m1+m2)/2
        else:
            median=li[n//2]
        return(median)