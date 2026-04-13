class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = []
        i = 0
        j = 0
        m = len(nums1) + len(nums2)
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merge.append(nums1[i])
                i += 1
            else:
                merge.append(nums2[j])
                j += 1
        merge.extend(nums1[i:])
        merge.extend(nums2[j:])
        if (m) % 2 == 0:
            left = (m//2)-1
            right = m//2
            return (merge[left] + merge[right])/2
        else:
            return merge[m//2]
