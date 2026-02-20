class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            smallest = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    smallest += 1
            output.append(smallest)
        return output
                    
        