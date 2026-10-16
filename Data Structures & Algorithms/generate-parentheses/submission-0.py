class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        def dfs(oCount, cCount, curSet):
            if oCount == n and cCount == n:
                self.res.append("".join(curSet))
                return
            if oCount < n:
                curSet.append("(")
                dfs(oCount + 1, cCount, curSet)
                curSet.pop()
            if cCount < oCount:
                curSet.append(")")
                dfs(oCount, cCount + 1, curSet)
                curSet.pop()
        dfs(0, 0, [])
        return self.res