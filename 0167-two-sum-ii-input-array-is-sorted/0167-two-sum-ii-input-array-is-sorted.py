class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]: #[2,7,11,15], 9
        left = 0 #0
        right = len(numbers) - 1
        
        while left < right:
            s = numbers[left] + numbers[right] 
            if s == target:
                return [left + 1, right + 1]
            if s < target:
                left += 1
            else:
                right -= 1
    
    
    # #Notes
    # - could use two pointers 
    #     - left - index
    #     - right - index
    # - while loop for left is less than right
    #     - add the two numbers at the array of left and right
    #     - compare sum to target
    #         - if the sum is greater than the target
    #             - decrement right index by one
    #         - if the sum is less than the target
    #             - increase left by one
    #         - if the sum == to target
    #             return [left, right]
            
    