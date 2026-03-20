class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        if sorted(nums) == nums:
            return 0
        oper = 0
        last = nums[-1]
        for i in range(len(nums) -2, -1,-1):
            if nums[i] > last:
                steps = (nums[i] - 1) // last + 1  
                last = nums[i] // steps
                oper += steps - 1
            else:
               
                last = nums[i]

        return oper

        