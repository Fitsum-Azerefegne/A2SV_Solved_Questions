class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        elements = {val: i for i, val in enumerate(nums1)}
        stack = []
        res = [-1] * len(nums1)

        for elem in nums2:
            while stack and stack[-1] < elem:
                less = stack.pop()
                if less in elements:
                    res[elements[less]] = elem
            stack.append(elem)

        return res