class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(candy):
            children = 0
            for c in candies:
                children += c // candy
            return children >= k
            
        if sum(candies) < k:
            return 0
        high = max(candies)
        low = 1
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                low = mid + 1
            else:
                high = mid - 1
        return high