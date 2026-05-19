class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        maxProfit = 0
        i = j = 0

        while i < len(nums) and j < len(nums):
            if nums[j] < nums[i]:
                i = j
            else:
                currProfit = nums[j] - nums[i]
                maxProfit = max(currProfit, maxProfit)
            j +=1

        return maxProfit