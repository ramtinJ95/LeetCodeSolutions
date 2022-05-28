from typing import List

nums = [-2,1,-3,4,-1,2,1,-5,4]
# answer is 6 for nums above.
# 

def maxSubArray(nums: List[int]) -> int:
    maxSumSoFar = nums[0]
    currentMax = 0
    
    for n in nums:
        if currentMax < 0:
            currentMax = 0
        currentMax += n
        maxSumSoFar = max(maxSumSoFar, currentMax)
    return maxSumSoFar

test = [-3, -1, -2000, -3000, -4000]
print(str(maxSubArray(test)))