class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = { 0: 1 }
        res = 0
        currSum = 0

        for n in nums:
            currSum += n
            diff = currSum - k
            res += prefixSum.get(diff, 0)
            prefixSum[currSum] = prefixSum.get(currSum, 0) + 1
        return res