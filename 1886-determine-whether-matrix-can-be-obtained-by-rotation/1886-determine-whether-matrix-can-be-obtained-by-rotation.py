class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        yes = False
        for _ in range(4):
            for i in range(n):
                for j in range(i, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
            for i in range(n):
                mat[i].reverse()
            if mat == target:
                yes = True
                break
        if yes:
            return True
        return False
            
            
        