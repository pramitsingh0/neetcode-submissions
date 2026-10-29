class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(i, r, c, visit) -> bool:
            
            if (min(r, c) < 0
                or r == ROWS or c == COLS
                or (r, c) in visit):
                return False
            
            if i < len(word) and board[r][c] != word[i]:
                return False

            if i == len(word) - 1 and board[r][c] == word[i]:
                return True
            visit.add((r, c))
            res = (dfs(i + 1, r + 1, c, visit)
                    or dfs(i + 1, r, c + 1, visit)
                    or dfs(i + 1, r - 1, c, visit)
                    or dfs(i + 1, r, c - 1, visit))
            visit.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c, set()):
                    return True
        return False
        
