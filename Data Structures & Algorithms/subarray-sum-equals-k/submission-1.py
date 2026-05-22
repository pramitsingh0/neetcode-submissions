class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixSum = { 0 : 1 }
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            diff = currSum - k
            res += prefixSum.get(diff, 0)
            prefixSum[currSum] = prefixSum.get(currSum, 0) + 1
        
        return res
