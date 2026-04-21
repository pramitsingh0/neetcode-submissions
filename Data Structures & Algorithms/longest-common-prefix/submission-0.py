class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        Given a list of string, find the longest prefix common between each of the strings
        """
        firstString = strs[0]
        res = ""
        for i, c in enumerate(firstString):
            for s in strs:
                if i == len(s) or s[i] != c:
                    return res
            res += firstString[i]
        return res