class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        nums1 = list(set(nums1))
        for a in nums1:
            if a in nums2:
                intersection.append(a)
        return intersection

        