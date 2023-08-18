class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                iL = 0
                iR = len(matrix[m]) - 1
                
                while iL <= iR:
                    iM = (iL + iR) // 2
                    if matrix[m][iM] == target:
                        return True
                    if matrix[m][iM] > target:
                        iR = iM - 1
                    else:
                        iL = iM + 1
                
                return False
            
            if matrix[m][0] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False
                