class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(i, curSet):
            if i >= len(s):
                res.append(curSet.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    curSet.append(s[i: j + 1])
                    backtrack(j + 1, curSet)
                    curSet.pop()
        backtrack(0, [])
        return res
    
    def isPalindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True
            