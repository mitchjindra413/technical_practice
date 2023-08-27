class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        prev = pairs[0]
        res = 1
        
        for i in range(1, len(pairs)):
            if pairs[i][0] > prev[1]:
                res += 1
                prev = pairs[i]
        
        return res