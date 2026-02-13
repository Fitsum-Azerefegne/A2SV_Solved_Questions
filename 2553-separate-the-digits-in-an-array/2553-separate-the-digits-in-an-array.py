class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        numbers = ""
        output = []
        for num in nums:
            numbers += str(num)
        for num in numbers:
            output.append(int(num))
        
        return output


        