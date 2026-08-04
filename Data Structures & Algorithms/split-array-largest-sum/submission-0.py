class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest: int) -> bool:
            splitCount = 1
            currSum = 0
            for n in nums:
                if currSum + n > largest:
                    splitCount += 1
                    currSum = 0
                currSum += n
            return splitCount <= k

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            candidate = l + (r - l) // 2

            if canSplit(candidate):
                res = min(res, candidate)
                r = candidate - 1
            else:
                l = candidate + 1
            
        return res