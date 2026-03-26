class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(i, com):
            if com not in res:
                res.append(com[:])
            for j in range(i, len(nums)):
                com.append(nums[j])
                backtrack(j + 1, com)
                com.pop()
        backtrack(0, [])
        return res