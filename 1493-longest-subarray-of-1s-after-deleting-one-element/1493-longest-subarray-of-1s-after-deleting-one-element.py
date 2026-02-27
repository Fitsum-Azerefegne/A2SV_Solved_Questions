class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums) - 1
        longest_subarray = 0
        left = 0
        zeros = 0
        ones = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            else:
                ones += 1
            while zeros > 1:
                if nums[left] == 0 :
                    zeros -= 1
                else:
                    ones -= 1
                left += 1
            longest_subarray = max(longest_subarray, ones)
        return longest_subarray
