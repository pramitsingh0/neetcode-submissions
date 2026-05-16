class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        res = 0
        people.sort()
        l, r = 0, len(people) - 1
        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <= r and people[l] <= remain:
                l += 1
        return res