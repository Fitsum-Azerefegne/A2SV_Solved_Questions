class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        # Initialize result matrix with zeros
        result = [[0] * n for _ in range(m)]
        
        # All directions including self
        directions = [
            (0, 0), (0, 1), (0, -1),
            (1, 0), (1, 1), (1, -1),
            (-1, 0), (-1, 1), (-1, -1)
        ]
        
        for r in range(m):
            for c in range(n):
                total = count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        total += img[nr][nc]
                        count += 1
                result[r][c] = total // count  # floor division
        return result