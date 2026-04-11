class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def firstposition(nums: List[int], target: int) ->int:
            left = 0
            right = len(nums) - 1 
            first = -1
            while left <= right:
                mid = (right + left)//2
                if nums[mid] == target:
                    first = mid
                    right = mid - 1
                elif nums[mid] > target:
                    right = mid -1
                else:
                    left = mid + 1
            return first
        def lastposition(nums: List[int], target: int) ->int:
            left = 0
            right = len(nums) - 1
            last = -1
            while left <= right:
                mid = (right + left)//2     
                if nums[mid] == target:
                    last = mid
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid -1
                else:
                    left = mid + 1
            return last
        first = firstposition(nums,target)
        last = lastposition(nums,target)
        return [first,last]
        

        