class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.prefix_sum = [[0 for i in range(m+1)] for j in range(n+1) ]
        for i in range(n):
            for j in range(m):
                self.prefix_sum[i][j] = matrix[i][j] + self.prefix_sum[i-1][j] + self.prefix_sum[i][j-1] - self.prefix_sum[i-1][j-1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        box = self.prefix_sum[row2][col2]
        left_box = self.prefix_sum[row2][col1-1]
        up_box = self.prefix_sum[row1-1][col2]
        overlap = self.prefix_sum[row1-1][col1-1]

        return box - left_box - up_box + overlap
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)