class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        summ = sum(num for num in nums if num % 2 == 0)
        sum_of_even = []
        for val, index in queries:
            old_val = nums[index]
            if old_val % 2 == 0:
                summ -= old_val
            nums[index] += val
            if nums[index] % 2 == 0:
                summ += nums[index]
            sum_of_even.append(summ)
        return sum_of_even
        