class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = set()
        for start, end in ranges:
            for n in range(start,end+1):
                covered.add(n)
        for n in range(left,right+1):
            if n not in covered:
                return False
        return True
