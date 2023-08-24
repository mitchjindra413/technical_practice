class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []
        length = 0
        
        for word in words:
            if len(word) + len(line) + length > maxWidth:
                diff = maxWidth - length
                spaces = diff // max(1, len(line) - 1)
                rem = diff % max(1, len(line) - 1)
                
                for i in range(max(1, len(line) - 1)):
                    line[i] += " " * spaces
                    
                    if rem:
                        line[i] += " "
                        rem -= 1
                
                res.append("".join(line))
                line = []
                length = 0
            
            line.append(word)
            length += len(word)
        
        last = " ".join(line)
        diff = maxWidth - len(last)
        res.append(last + " " * diff)
        
        return res