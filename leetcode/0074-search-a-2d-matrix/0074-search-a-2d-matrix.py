class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = (len(matrix[0])*len(matrix)) - 1
        n = len(matrix[0])
        while low <= high:
            mid = (low + high )//2
            row = mid // n
            col = mid % n
            value = matrix[row][col]
            if value > target:
                high = mid - 1
            elif value < target:
                low = mid + 1
            else:
                return True
        return False
        