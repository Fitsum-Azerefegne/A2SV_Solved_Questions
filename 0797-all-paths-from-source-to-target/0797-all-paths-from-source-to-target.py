
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        result = []    
        queue = deque([(0, [0])])  # (current_node, path)

        while queue:
            node, path = queue.popleft()

            if node == target:
                result.append(path)
                continue

            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))

        return result