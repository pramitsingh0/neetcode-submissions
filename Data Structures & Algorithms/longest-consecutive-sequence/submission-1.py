class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums)
        longest = 0
        for num in nums:
            length = 1
            if num - 1 not in nums:
                
                while num + length in nums:
                    length += 1
            longest = max(length, longest)
        return longest