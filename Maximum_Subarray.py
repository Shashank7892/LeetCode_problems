def maxSubArray(nums):
    cmax=nums[0]
    maxi=nums[0]

    for i in range(1,len(nums)):
        cmax=max(nums[i],cmax+nums[i])
        if cmax > maxi:
            maxi=cmax
    return maxi


nums=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))