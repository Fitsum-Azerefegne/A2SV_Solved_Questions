class Solution:
    def generate(self, numRows: int) -> List[List[int]]: 
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            triangle = self.generate(numRows - 1)
            row = [1] * numRows
            for j in range(1, numRows - 1):
                row[j] = triangle[-1][j - 1] + triangle[-1][j] 
            triangle.append(row)
            return triangle
    def getRow(self, rowIndex: int) -> list[int]:
        triangle = self.generate(rowIndex + 1)
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            return triangle[rowIndex]