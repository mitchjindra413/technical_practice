class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        res = []
        
        start = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 != nums[i]:
                if nums[i - 1] == start:
                    res.append(f'{start}')
                else:
                    res.append(f'{start}->{nums[i-1]}')
                
                start = nums[i]
        
        if nums[-1] == start:
            res.append(f'{start}')
        else:
            res.append(f'{start}->{nums[-1]}')
                
        return res