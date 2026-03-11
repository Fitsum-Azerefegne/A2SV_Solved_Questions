from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deq = deque()
        min_deq = deque()
        left, right = 0, 0
        res = 0

        for right , num in enumerate(nums):
            while max_deq and nums[max_deq[-1]] < num:
                max_deq.pop()
            max_deq.append(right)
            while min_deq and nums[min_deq[-1]] > num:
                min_deq.pop()
            min_deq.append(right)
            while nums[max_deq[0]] - nums[min_deq[0]] > limit:
                if max_deq[0] == left:
                    max_deq.popleft()
                if min_deq[0] == left:
                    min_deq.popleft()
                left += 1

            res = max(res, right - left + 1)
        return res            


        