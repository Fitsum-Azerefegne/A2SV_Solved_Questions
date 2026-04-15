class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        out = []
        for n in nums:
            if n in seen:
                out.append(n)
            seen.add(n)
        for i in range(1,len(nums)+1):
            if i not in nums:
                out.append(i)
        return out




        