class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        res = float("-inf")
        
        for num in nums:
            currSum += num
            res = max(res, currSum)
            
            if currSum < 0:
                currSum = 0
                
        return res