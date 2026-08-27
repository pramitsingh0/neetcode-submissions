class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        for i, a in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                currThreeSum: int = a + nums[l] + nums[r]

                if currThreeSum > 0:
                    r -= 1
                elif currThreeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res