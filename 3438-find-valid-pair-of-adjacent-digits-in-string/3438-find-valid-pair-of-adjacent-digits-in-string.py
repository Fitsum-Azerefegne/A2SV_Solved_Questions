class Solution:
    def findValidPair(self, s: str) -> str:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1

        for i in range(len(s) - 1):
            a, b = s[i], s[i + 1]

            if (
                a != b and
                a.isdigit() and b.isdigit() and
                freq[a] == int(a) and
                freq[b] == int(b)
            ):
                return a + b

        return ""
