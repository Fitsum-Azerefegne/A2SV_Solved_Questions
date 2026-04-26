class Solution:
    def solve(self, board: List[List[str]]) -> None: 
        # start from borders do dfs if 0 make to s 
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        row = len(board)
        col = len(board[0])
        def inbound(r,c):
            return 0 <= r < row and 0 <= c < col
        def dfs(r,c):
            board[r][c] = "S"
            for dx, dy in directions:
                nx = r + dx
                ny = c + dy
                if inbound(nx,ny) and board[nx][ny] == "O":
                    dfs(nx,ny)

        for r in range(row):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][col - 1] == "O":
                dfs(r, col - 1)

        for c in range(col):
            if board[0][c] == "O":
                dfs(0, c)
            if board[row - 1][c] == "O":
                dfs(row - 1, c)

        for r in range(row):
            for c in range(col):
                if board[r][c] == "S":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"

