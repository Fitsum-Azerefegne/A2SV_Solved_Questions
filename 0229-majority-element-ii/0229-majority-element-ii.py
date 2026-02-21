class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = len(nums) // 3
        hash_map = defaultdict(int)
        output = []
        for n in nums:
            hash_map[n] += 1
        for n in nums:
            if hash_map[n] > freq:
                output.append(n)
        return list(set(output))
        