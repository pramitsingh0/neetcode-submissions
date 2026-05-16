class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l, r = 0, len(heights) - 1
        maxWaterContainer = 0
        while l < r:
            currWaterContainer = (r - l) * (min(heights[l], heights[r]))
            maxWaterContainer = max(currWaterContainer, maxWaterContainer)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxWaterContainer