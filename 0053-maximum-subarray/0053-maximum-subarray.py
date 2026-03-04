class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_prefix_sum = 0
        min_prefix_sum = 0
        max_sum = float("-inf")
        for num in nums:
            curr_prefix_sum += num
            max_sum = max(max_sum, curr_prefix_sum - min_prefix_sum)
            min_prefix_sum = min(min_prefix_sum, curr_prefix_sum)
        return max_sum    
            