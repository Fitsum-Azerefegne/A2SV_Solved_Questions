class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0,0,0]
        for num in nums:
            count[num] += 1
        index = 0
        print(count)
        for i in range(3):
            for _ in range(count[i]):
                nums[index] = i
                index += 1