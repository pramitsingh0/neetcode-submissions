class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        def dfs(openN, closeN, curSet):
            if openN == n and closeN == n:
                self.res.append("".join(curSet))
                return
            
            if openN < n:
                curSet.append("(")
                dfs(openN + 1, closeN, curSet)
                curSet.pop()
            if closeN < openN:
                curSet.append(")")
                dfs(openN, closeN + 1, curSet)
                curSet.pop()
        dfs(0, 0, [])
        return self.res
        
