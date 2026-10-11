class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.count = collections.Counter(nums)
        self.res = []
        
        def dfs(curPerm):
            if len(curPerm) == len(nums):
                self.res.append(curPerm.copy())
                return
            
            for n in self.count:
                if self.count[n]:
                    curPerm.append(n)
                    self.count[n] -= 1

                    dfs(curPerm)

                    curPerm.pop()
                    self.count[n] += 1
        dfs([])
        return self.res