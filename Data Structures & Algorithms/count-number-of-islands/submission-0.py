class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        islands = 0
        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            
            while q:
                r, c = q.popleft()

                neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in neighbours:
                    nr = r + dr
                    nc = c + dc
                    
                    if (min(nr, nc) < 0
                        or nr == ROWS or nc == COLS
                        or (nr, nc) in visit
                        or grid[nr][nc] == "0"):
                        continue
                    q.append((nr, nc))
                    visit.add((nr, nc))
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands