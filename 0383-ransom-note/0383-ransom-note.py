class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        noteCount = collections.Counter(ransomNote)
        magCount = collections.Counter(magazine)
        
        for k, v in noteCount.items():
            if magCount[k] < v:
                return False
        
        return True