class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        allowed_skips = 1
        while l < r:
            if s[l] != s[r]:
                allowed_skips -= 1
                if allowed_skips < 0:
                    return False
                if s[l] == s[r - 1]:
                    r = r - 1
                elif s[r] == s[l + 1]:
                    l = l + 1
            l += 1
            r -= 1
            
        return True