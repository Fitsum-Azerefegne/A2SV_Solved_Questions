from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        freq = defaultdict(int)
        freq[0] = 1  
        for num in nums:
            prefix += num
            remainder = prefix % k
            remainder = remainder if remainder >= 0 else remainder + k  
            count += freq[remainder]
            freq[remainder] += 1
        
        return count