class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = [[] for _ in range(n)]
      
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, _ = bombs[j]
                dist2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
                if dist2 <= r1 * r1:
                    graph[i].append(j)
        
        def dfs(start: int) -> int:
            stack = [start]
            visited = [False] * n
            visited[start] = True
            count = 0
            while stack:
                u = stack.pop()
                count += 1
                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            return count

        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))
        
        return ans