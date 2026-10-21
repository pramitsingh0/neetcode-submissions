class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))

        def bfs(q):
            minutes = 0
            while q:
                qLen = len(q)
                updated = False
                for i in range(qLen):
                    r, c = q.popleft()
                    if grid[r][c] == 1:
                        grid[r][c] = 2
                        updated = True
                    for dr, dc in neighbors:
                        nr, nc = r + dr, c + dc
                        if (min(nr, nc) < 0
                            or nr == ROWS or nc == COLS
                            or (nr, nc) in visit
                            or grid[nr][nc] != 1):
                            continue
                        q.append((nr, nc))
                        visit.add((nr, nc))
                if updated:
                    minutes += 1
            return minutes
        minutes = bfs(q)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return minutes

