
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(capacity):
            day = 1
            curr_sum = 0
            for w in weights:
                curr_sum += w
                if curr_sum > capacity:
                    day += 1
                    curr_sum = w
                    if day > days:
                        return False
            return day <= days
        
        high = sum(weights)
        low = max(weights)

        while low < high:
            mid = (low + high) // 2
            if check(mid):
                high = mid
            else:
                low = mid + 1
        return low