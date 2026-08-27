class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = 0
        res = 0
        while j < len(s):
            currSubstringLength = 0
            encounteredSet = set()
            while j < len(s) and not s[j] in encounteredSet:
                encounteredSet.add(s[j])
                j += 1
                
            currSubstringLength = j - i
            res = max(currSubstringLength, res)
            i = j
        
        return res
     