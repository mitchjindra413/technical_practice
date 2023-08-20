/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let seen = new Set();
    let res = 0
    let start = 0
    
    for (i = 0; i < s.length; i++) {
        while (seen.has(s[i])) {
            seen.delete(s[start])
            start ++
        }
        seen.add(s[i])
        res = Math.max(res, i - start + 1)
    }
    
    return res
    
};