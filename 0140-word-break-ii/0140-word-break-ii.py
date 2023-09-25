class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dictionary = set(wordDict)
        memo = {}
        
        def explore(s):
            if not s: return [[]]
            if s in memo: return memo[s]
            
            res = []
            
            for end in range(1, len(s) + 1):
                currWord = s[:end]
                
                if currWord in dictionary:
                    prevArr = explore(s[end:])
                    for sub in prevArr:
                        res.append([currWord, *sub])
            
            memo[s] = res
            return res
        
        return [" ".join(words) for words in explore(s)]
        
        
#     Notes:
#         function (start)
#             if start >= lenght of s: return []
#             currWord = slice from start to end
            
#             res = []
#                 [[cats, and, dog], [ cat, sand, dog]]
            
#             for end in range from start to length of s
#                 currWord = slice of start to end
            
#                 if currWord is in wordDict:
#                     prevArr = call function increaing start = end + 1
#                     res.push [currWord, *prevArr]
                  
            
#             return res
            
                
        