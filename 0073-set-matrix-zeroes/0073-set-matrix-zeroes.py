class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        zeros = []
    
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zeros.append((i, j))
        
        for r, c in zeros:
            for j in range(cols):
                matrix[r][j] = 0
            for i in range(rows):
                matrix[i][c] = 0