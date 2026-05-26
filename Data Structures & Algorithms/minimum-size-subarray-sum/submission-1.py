class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur_sum = 0
        l = 0
        res = float('inf')

        for r in range(len(nums)):
            cur_sum += nums[r]
            while cur_sum >= target:
                res = min(r - l + 1, res)
                cur_sum -= nums[l]
                l += 1

        return 0 if res == float('inf') else res 
        

