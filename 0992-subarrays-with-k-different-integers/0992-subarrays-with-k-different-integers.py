class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(k):
            left = 0
            count = defaultdict(int)
            result = 0
            
            for right in range(len(nums)):
                count[nums[right]] += 1
                
                while len(count) > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1
                
                result += right - left + 1
            return result  
        return atMostK(k) - atMostK(k-1)