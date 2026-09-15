from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        fresh = 0
        visited = set()
        q = deque()
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if (nr >= 0 and nc >= 0 and nr < ROWS and nc < COLS
                    and (nr, nc) not in visited and grid[nr][nc] == 1):
                        fresh -= 1
                        visited.add((nr, nc))
                        q.append((nr, nc))
            time += 1
        
        return time if fresh == 0 else -1

        