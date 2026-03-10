class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1 
        running_sum = 0
        result = 0
        
        for num in nums:
            running_sum += num
            result += prefix_count[running_sum - goal]
            prefix_count[running_sum] += 1        
        return result     