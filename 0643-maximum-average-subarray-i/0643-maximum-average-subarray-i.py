class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
         i = 0
         summ = sum(nums[:k])
         max_sum = summ
         for j in range(k, len(nums)):
            summ = summ - nums[i] + nums[j] 
            i += 1
            max_sum = max(max_sum,summ)
         return max_sum / k
        