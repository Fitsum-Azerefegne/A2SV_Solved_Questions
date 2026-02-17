class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split()
        if len(pattern) != len(arr):
            return False
        dd = defaultdict(str)
        for i in range(len(pattern)):
            if arr[i] in dd.values() and pattern[i] not in dd :
                return False
            if pattern[i] in dd:
                if dd[pattern[i]] != arr[i]:
                    return False
            dd[pattern[i]] = arr[i]
        return True
        