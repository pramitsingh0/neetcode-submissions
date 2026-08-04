class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = { 0: 1 }
        currSum = 0
        res = 0
        for r in range(len(nums)):
            currSum += nums[r]

            diff = currSum - k
            if diff in prefixSum:
                res += prefixSum[diff]
            prefixSum[currSum] = prefixSum.get(currSum, 0) + 1 
        return res