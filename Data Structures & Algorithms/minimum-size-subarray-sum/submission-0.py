class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur_sum = 0
        l = 0
        res = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            if cur_sum >= target:
                if res == 0:
                    res = r - l + 1
                res = min(res, r - l + 1)
                while l < r:
                    cur_sum -= nums[l]
                    if cur_sum < target:
                        res = min(res, r - l + 1)
                        break
                    l += 1
        
        return res
