class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        result = []
        num_rows = len(mat)
        num_columns = len(mat[0])
        
       
        for diag in range(num_rows + num_columns - 1):
            if diag % 2 == 0:  
                row = min(diag, num_rows - 1)
                col = diag - row
                
                while row >= 0 and col < num_columns:
                    result.append(mat[row][col])
                    row -= 1
                    col += 1
            else:  
                col = min(diag, num_columns - 1)
                row = diag - col
                
                while row < num_rows and col >= 0:
                    result.append(mat[row][col])
                    row += 1
                    col -= 1
        
        return result