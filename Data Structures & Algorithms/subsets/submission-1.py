class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.subsets = []

        def dfs(i, curSet):
            if i == len(nums):
                self.subsets.append(curSet.copy())
                return
            
            curSet.append(nums[i])
            dfs(i + 1, curSet)
            curSet.pop()
            dfs(i + 1, curSet)
        
        dfs(0, [])
        return self.subsets
            