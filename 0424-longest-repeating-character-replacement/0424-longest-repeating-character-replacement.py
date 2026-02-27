class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_map = defaultdict(int)
        max_freq = 0
        longest = 0
        left = 0
        for right in range(len(s)):
            count_map[s[right]] += 1
            max_freq = max(max_freq, count_map[s[right]])
            while  (right - left + 1) - max_freq > k:
                count_map[s[left]] -= 1
                left += 1
            longest = max(longest, right - left+1)
        return longest