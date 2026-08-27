class Solution:
    def trap(self, height: list[int]) -> int:
        res = 0
        l = 0
        r = 0
        while r < len(height) and l < len(height):
            # let l be local maxima for current 
            while height[l] == 0:
                l += 1
            r = l + 1
            while r < len(height) - 1 and (height[r + 1] > height[r] or height[r] == 0):
                r += 1
            res += min(height[l], height[r]) * (l - r)
            l = r
            
        return res