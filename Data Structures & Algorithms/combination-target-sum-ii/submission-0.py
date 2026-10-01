class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()

        self.res = []

        def dfs(i, curSet, curSum):
            if curSum == target:
                self.res.append(curSet.copy())
                return
            if curSum > target or i >= len(candidates): return
            
            
            curSet.append(candidates[i])
            dfs(i + 1, curSet, curSum + candidates[i])
            curSet.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curSet, curSum)
        dfs(0, [], 0)

        return self.res