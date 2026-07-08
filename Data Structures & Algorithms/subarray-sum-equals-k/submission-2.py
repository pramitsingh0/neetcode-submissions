class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        res = 0
        prefix_sum = { 0: 1}

        for r in range(len(nums)):
            cur_sum += nums[r]
            diff = cur_sum - k
            res += prefix_sum.get(diff, 0)
            prefix_sum[cur_sum] = prefix_sum.get(cur_sum, 0) + 1
        return res
            