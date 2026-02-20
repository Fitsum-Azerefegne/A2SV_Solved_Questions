class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))   
        print(nums_str)
        for i in range(len(nums_str)):
            for j in range(i + 1, len(nums_str)):   
                if nums_str[i] + nums_str[j] < nums_str[j] + nums_str[i]:
                    nums_str[i], nums_str[j] = nums_str[j], nums_str[i]
        
        result = ''.join(nums_str)
        
        return '0' if result[0] == '0' else result 