class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        row = len(grid)
        col = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        def inbound(r,c):
            return 0 <= r < row and 0 <= c < col  
        def dfs(r,c):
            grid[r][c] = "0"
            for dx, dy in directions:
                nx = r + dx
                ny = c + dy
                if inbound(nx,ny) and grid[nx][ny]== "1":
                    dfs(nx,ny)
            
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r,c)

        return islands
        