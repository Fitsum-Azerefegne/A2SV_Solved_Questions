class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        dd = defaultdict(int)
        output = 0
        maximum_output = 0
        for right in range(len(s)):
            dd[s[right]] += 1
            output += 1
            
            while dd[s[right]] > 1:
                dd[s[left]] -= 1
                left += 1
                output -= 1
            maximum_output = max(maximum_output, output)
        return maximum_output
                