class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) < 3: return 0
        
        nums.sort()
        res = 0
        
        for first in range(len(nums) - 2):
            second = first + 1
            third = len(nums) - 1
            while second < third:
                three_sum = nums[first] + nums[second] + nums[third]
                if three_sum < target:
                    res += third - second
                    second += 1
                else:
                    third -= 1

        return res