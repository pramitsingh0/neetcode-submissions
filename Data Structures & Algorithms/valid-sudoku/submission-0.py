from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        m = len(board)
        n = len(board[0])
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        box_map = defaultdict(set)

        for r in range(m):
            for c in range(n):
                if board[r][c] == ".":
                    continue
                if board[r][c] in col_map[c] or board[r][c] in row_map[r] or board[r][c] in box_map[tuple([r//3, c//3])]:
                    return False

                col_map[c].add(board[r][c])
                row_map[r].add(board[r][c])
                box_map[tuple([r//3, c//3])].add(board[r][c])

        return True