class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        s_count, t_count = {}, {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
        
        l = 0
        have = 0
        need = len(t_count)
        res = [-1, -1]
        resLen = float("inf")
        for r in range(len(s)):
            c = s[r]
            s_count[c] = s_count.get(c, 0) + 1
            if c in t_count and s_count[c] == t_count[c]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                s_count[s[l]] -= 1
                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l : r + 1] if resLen != float("inf") else ""
