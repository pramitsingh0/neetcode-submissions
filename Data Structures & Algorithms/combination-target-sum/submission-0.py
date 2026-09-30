class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []

        def dfs(i, curSet, total):
            if total > target:
                return
            if sum(curSet) == target:
                self.res.append(curSet.copy())
                return
            
            for j in range(i, len(nums)):
                # if total + nums[j] > target: return 
                curSet.append(nums[j])
                dfs(j, curSet, total + nums[j])
                curSet.pop()
        dfs(0, [], 0)
        return self.res
