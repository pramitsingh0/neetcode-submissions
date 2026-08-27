class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def hoursToEatBananas(k: int):
            hours = 0

            for p in piles:
                hours += math.ceil(p / k)
            return hours

        
        l, r = 1, max(piles)
        while l <= r:
            k = (l + r) // 2
            if hoursToEatBananas(k) <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
            
        return l
            
