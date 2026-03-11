from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        res = []
        for i, num in enumerate(nums): 
            while deq and nums[deq[-1]] < num:
                deq.pop()
            deq.append(i)
            if deq[0] <= i - k:
                deq.popleft()
            if i >= k - 1:
                res.append(nums[deq[0]])
        return res
        