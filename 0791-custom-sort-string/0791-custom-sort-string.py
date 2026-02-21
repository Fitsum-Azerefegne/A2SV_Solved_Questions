class Solution:
    def customSortString(self, order: str, s: str) -> str:
        start = ""
        end = ""
        hash_s = defaultdict(int)
        for j in s:
            hash_s[j] += 1

        for letter in order:
            if letter in s:
                start += letter * hash_s[letter]

        
        for letter in s:
            if letter not in start and hash_s[letter] > 0:
                end += letter
        return start + end

        