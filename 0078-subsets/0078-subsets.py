class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]: 
        if not nums: return [[]] 
        
        prev = self.subsets(nums[1:]) 
        
        newSubsets = [] 
        
        for sub in prev: 
            newSubsets.append([nums[0], *sub]) 
        
        return prev + newSubsets 
    
# Notes:
# - recursion
# - Base Case:
#     - if nums is [] -> return [[]]

# - store previous case
# - iterate through all of the prvious values in the array
#     - add our current number to that element
# - return prev + new array

#  prev = subsets(nums[1:])
#  new = []
#  curr = nums[0]
#  for each element of prev:
#     append to new element + current number
    
#  return prev + new

#  [1]

#  prev = [[]]
#  new [[1]]
#  return prev + new = [[], [1]]


#  set base case to be if nums = []: return [[]]
#  find our previous recursive cases: subsets(nums[1:])
#  set up new array
#  add current iteration to all of previous arrays
#  return the prev array + new array