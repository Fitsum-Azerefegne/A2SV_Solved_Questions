class Solution:
    def smallestPalindrome(self, s: str) -> str:
        length = len(s)
        half_s = s[:]
        output = ""
        if length % 2 == 0:
            halve = s[:length//2]
            halve = sorted(halve)
            output = halve + list(reversed(halve))
        else:
            halve = s[:length//2]
            halve = sorted(halve)
            middle = s[length//2]
            output = halve + [middle] + list(reversed(halve))

        return("".join(output))

        