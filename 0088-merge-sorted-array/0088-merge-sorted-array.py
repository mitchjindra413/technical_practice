class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = len(nums1) - 1
        i = len(nums1) - len(nums2) - 1
        j = len(nums2) - 1
        
        while j >= 0 and i>= 0:
            if nums2[j] >= nums1[i]:
                nums1[p] = nums2[j]
                j -= 1
            else:
                nums1[p] = nums1[i]
                i -= 1
            p -= 1
            
        while j >= 0:
            nums1[p] = nums2[j]
            j -= 1
            p-= 1
            
        return nums1