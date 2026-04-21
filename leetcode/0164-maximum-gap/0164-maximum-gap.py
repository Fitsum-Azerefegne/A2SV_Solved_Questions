class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        max_dif = 0
        nums.sort()
        first = nums[0]
        for i in range(1,len(nums)):
            max_dif = max( max_dif, nums[i] - first)
            first = nums[i]
        return max_dif
        