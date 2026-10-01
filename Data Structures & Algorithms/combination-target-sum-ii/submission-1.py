class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()

        self.res = []

        def dfs(idx, curSet, curSum):
            if curSum == target:
                self.res.append(curSet.copy())
                return
            
            # curSet.append(candidates[i])
            # dfs(i + 1, curSet, curSum + candidates[i])
            # curSet.pop()
            # while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            #     i += 1
            # dfs(i + 1, curSet, curSum)
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] + curSum > target:
                    break
                curSet.append(candidates[i])
                dfs(i + 1, curSet, curSum + candidates[i])
                curSet.pop()
            
        dfs(0, [], 0)

        return self.res