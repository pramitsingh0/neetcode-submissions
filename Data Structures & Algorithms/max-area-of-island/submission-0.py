class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        maxArea = 0
        def dfs(r, c):
            if (min(r, c) < 0
                or r == ROWS or c == COLS
                or grid[r][c] != 1
                or (r, c) in visit):
                return 0
            
            visit.add((r, c))
            area = grid[r][c]
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                area += dfs(nr, nc)
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = dfs(r, c)
                    maxArea = max(area, maxArea)
        
        return maxArea