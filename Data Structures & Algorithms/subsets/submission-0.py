class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.subsets = []

        def dfs(i, nums, curSet):
            if i == len(nums):
                self.subsets.append(curSet.copy())
                return
            
            curSet.append(nums[i])
            dfs(i + 1, nums, curSet)
            curSet.pop()
            dfs(i + 1, nums, curSet)
        
        dfs(0, nums, [])
        return self.subsets
            