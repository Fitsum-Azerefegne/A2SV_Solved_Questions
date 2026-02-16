class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count = Counter(nums)
        dominant = count.most_common(1)[0][0]
        total = count.most_common(1)[0][1]
        total_size = len(nums)
        if total * 2 < total_size :
            return False
        
        left_count = 0
        
        
        for i in range(total_size - 1):
            if nums[i] == dominant:
                left_count += 1
            right_count = total - left_count
            left_size = i + 1
            right_size = total_size - left_size

            if right_count * 2 > right_size and left_count * 2 > left_size:
                return i
        return -1
