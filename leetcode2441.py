# 2441. Largest Positive Integer That Exists With Its Negative
def findmaxk(nums):
    nums.sort()
    for i in range(len(nums)-1,-1,-1):
        x=-nums[i]
        if x in nums:
            return abs(x)
            break
    else:
        return -1
    
    
# nums=[-1,2,-3,3] #output:3
# nums=[-10,8,6,7,-2,-3] #output:-1
nums=[-1,10,6,7,-7,1] #output:7
print(findmaxk(nums))