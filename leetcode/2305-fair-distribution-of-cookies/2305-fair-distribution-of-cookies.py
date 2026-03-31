class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        min_unfair = float("inf")
        dist = [0] * k
        def backtrack(i):
            nonlocal min_unfair, dist
            if i == len(cookies):
                min_unfair = min(min_unfair, max(dist))
                return
            if min_unfair <= max(dist):
                return
            for j in range(k):
                dist[j] += cookies[i]
                backtrack(i+1)
                dist[j] -= cookies[i]

        backtrack(0)
        return min_unfair
        