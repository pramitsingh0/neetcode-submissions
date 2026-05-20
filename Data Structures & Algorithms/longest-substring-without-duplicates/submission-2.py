class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        encounteredSet = set()
        i = j = 0
        res = 0
        
        while j < len(s):
            while s[j] in encounteredSet:
                encounteredSet.remove(s[i])
                i += 1
            encounteredSet.add(s[j])
            res = max(res, (j - i + 1))
            j += 1
        return res
