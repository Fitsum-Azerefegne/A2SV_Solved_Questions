class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        s = 0
        min_sum = 0
        
        for n in nums:
            s += n
            min_sum = min(min_sum, s)
        
        return 1 - min_sum
        