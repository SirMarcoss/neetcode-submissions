class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[1,0], [-1,0],[0,1],[0,-1]]
        visited = set()
        
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or board[r][c] != 'O'):
                return
            
            visited.add((r,c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
        
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS -1)
        
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited:
                    board[r][c] = 'X'
        
            
            
        

        
        