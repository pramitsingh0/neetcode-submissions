class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ROWS = len(board)
        self.COLS = len(board[0])
        def dfs(r, c, i, visit):
            if (i == len(word)
                or min(r, c) < 0
                or (r,c) in visit
                or r == self.ROWS or c == self.COLS):
                return False
            nextChar = word[i]
            if board[r][c] != nextChar: return False

            if i == len(word) - 1:
                return True
            
            visit.add((r, c))
            res = (dfs(r + 1, c, i + 1, visit)
                    or dfs(r, c + 1, i + 1, visit)
                    or dfs(r - 1, c, i + 1, visit)
                    or dfs(r, c - 1, i + 1, visit))
            visit.remove((r, c))

            return res
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if dfs(r, c, 0, set()):
                    return True
        return False


            