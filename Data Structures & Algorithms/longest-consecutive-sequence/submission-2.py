class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        res = 0
        nums_set = set()
        for n in nums:
            nums_set.add(n)

        for n in nums:
            count = 1
            curr = n
            while curr + 1 in nums_set:
                count += 1
                curr += 1

            res = max(count, res)


        return res