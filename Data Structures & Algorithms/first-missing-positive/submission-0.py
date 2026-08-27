class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            val = abs(nums[i])
            if val >= 1 and val <= len(nums):
                if nums[i] >= 0:
                    nums[i] *= -1
                elif nums[i] == 0:
                    nums[i] = -1 * (len(nums) + 1)
            
        for i in range(1, len(nums) + 1):
            idx = i - 1
            if nums[idx] > 0:
                return i

        return len(nums) + 1