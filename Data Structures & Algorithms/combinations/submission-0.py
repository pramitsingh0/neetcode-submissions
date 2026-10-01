class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.results = []

        def dfs(i, curSet):
            if len(curSet) == k:
                self.results.append(curSet.copy())
                return
            
            for j in range(i, n + 1):
                curSet.append(j)
                dfs(j + 1, curSet)
                curSet.pop()
        dfs(1, [])
        return self.results