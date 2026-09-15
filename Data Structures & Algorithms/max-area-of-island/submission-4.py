class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        visited = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0
            or (r, c) in visited):
                return 0
            
            res = 1
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                res += dfs(nr, nc)
            
            return res
        
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = max(area, dfs(r, c))
        return area

        