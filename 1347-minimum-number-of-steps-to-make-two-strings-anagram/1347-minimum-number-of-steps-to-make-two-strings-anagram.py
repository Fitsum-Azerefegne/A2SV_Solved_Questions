class Solution:
    def minSteps(self, s: str, t: str) -> int:
        t_count = Counter(t)
        s_count = Counter(s)
        steps = 0
        if t_count == s_count:
            return 0
        for letter in s_count:
            if s_count[letter] > t_count[letter]:
                steps += s_count[letter] - t_count[letter]
        return steps
     