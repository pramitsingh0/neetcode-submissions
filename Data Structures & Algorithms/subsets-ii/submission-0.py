class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        self.res = []
        nums.sort()
        def dfs(i: int, curSet: list[int]) -> None:
            if i >= len(nums):
                self.res.append(curSet.copy())
                return
            
            curSet.append(nums[i])
            dfs(i + 1, curSet)
            curSet.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, curSet)
        dfs(0, [])
        return self.res
