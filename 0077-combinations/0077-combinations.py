class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [o for o in range(1,n+1)]
        res = []

        def backtrack(i, path):
            if len(path) == k:
                res.append(path[:])
                return
            if i >= n:
                return
            path.append(nums[i])
            backtrack(i+1, path )
            path.pop()

            backtrack(i+1, path)
        backtrack(0,[])
        return res