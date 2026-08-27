class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        cur_max = 0

        for r in range(len(nums)):
            cur_max = max(nums[r], cur_max)
            if r - l + 1 == k:
                res.append(cur_max)
                if nums[l] == cur_max:
                    cur_max = nums[min(l + 1, len(nums))]
                l += 1
        return res

