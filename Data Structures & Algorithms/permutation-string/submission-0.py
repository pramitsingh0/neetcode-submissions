class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1

        while r < len(s2):
            
            windowSet = set(list(s2[l : r + 1]))
            
            containsAll = True
            for c in s1:
                if c not in windowSet:
                    containsAll = False
                    break
            
            if containsAll:
                return True
            
            r += 1
            l += 1
        return False
