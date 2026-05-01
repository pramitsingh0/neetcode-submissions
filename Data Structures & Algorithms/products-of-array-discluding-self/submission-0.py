class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix_num = 1
        postfix_num = 1
        res = [0] * len(nums)
        n = len(nums)

        for i in range(n):
            res[i] = prefix_num * nums[i]
            prefix_num *= nums[i]

        for i in range(n - 1, -1, -1):
            prefix_prod = res[i - 1] if i - 1 >= 0 else 1
            res[i] = postfix_num * prefix_prod
            postfix_num *= nums[i]

        return res
        