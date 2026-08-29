class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = { 0: 1 }
        curSum = 0
        res = 0
        for n in nums:
            curSum += n
            diff = curSum - k
            res += prefix.get(diff, 0)
            prefix[curSum] = prefix.get(curSum, 0) + 1

        return res