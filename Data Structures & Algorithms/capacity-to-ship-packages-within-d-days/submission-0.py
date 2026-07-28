class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def daysToShip(capacity: int) -> int:
            daysCount = 1
            currWeight = 0
            for w in weights:
                if currWeight + w > capacity:
                    daysCount += 1
                    currWeight = 0
                currWeight += w
            return daysCount
        
        l, r = max(weights), sum(weights)
        res = r
        while l <= r:
            cap = (l + r) // 2

            if daysToShip(cap) <= days:
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        
        return res
