class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid: return 
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = collections.deque()
        INF = 2147483647
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
        
        def bfs(q):
            length = 0
            while q:
                qLen = len(q)
                for i in range(qLen):
                    r, c = q.popleft()
                    neighbors = [(1, 0), (-1, 0), (0, -1), (0, 1)]

                    grid[r][c] = length
                    for dr, dc in neighbors:
                        nr, nc = r + dr, c + dc
                        if (min(nr, nc) < 0
                            or nr == ROWS or nc == COLS
                            or grid[nr][nc] != INF
                            or (nr, nc) in visit):
                            continue
                        q.append((nr, nc))
                        visit.add((nr, nc))
                length += 1
        bfs(q)





