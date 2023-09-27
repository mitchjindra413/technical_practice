class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        
        res = sorted(count, key = lambda x: (-count[x], x))
        
        return res[:k]