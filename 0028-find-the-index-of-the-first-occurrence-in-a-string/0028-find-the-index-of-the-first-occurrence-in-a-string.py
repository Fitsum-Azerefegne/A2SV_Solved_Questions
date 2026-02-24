class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = 0
        h = 0
        while n< len(needle) and h < len(haystack):
            if haystack[h] == needle[n]:
                h += 1
                n += 1
                if n == len(needle):
                    return h - len(needle)
            else:
                h = h - n + 1   
                n = 0
        return -1
        