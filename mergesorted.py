class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        a=len(nums1)-m
        b=len(nums2)-n
        for i in range(a):
            nums1.remove(nums1[-1])
        for j in range(b):
            nums2.remove(nums2[-1])
        for i in nums2:
            nums1.append(i)
        nums1.sort()