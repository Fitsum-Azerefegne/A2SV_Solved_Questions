class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dir = [(0,1), (1,0),(-1,0),(0,-1)]
        
        def is_inbound(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
            
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid [i][j] == 2:
                    queue.append(((i,j),0))
        mx = 0

        while queue:
            coord, time = queue.popleft()
            for xi, yi in dir:
                newi, newj = coord[0] +xi, coord[1]+yi
                if is_inbound(newi,newj) and grid[newi][newj] == 1:
                    queue.append(((newi,newj), time +1))
                    grid[newi][newj] = 0 
                    mx = max(time+1, mx)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] ==1:
                    return -1
            
        return mx