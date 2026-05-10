class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        def swap(i, j):
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp

        while l < r:
            swap(l, r)
            l += 1
            r -= 1