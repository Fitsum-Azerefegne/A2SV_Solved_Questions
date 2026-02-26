class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_map = defaultdict(int)
        for i in range(len(s)):
            last_map[s[i]] = i
        partitions = []
        start, end = 0, 0
        for index, char in enumerate(s):
            end = max(end, last_map[char])
            if index == end:
                partitions.append(end - start + 1)
                start = index + 1
        return partitions



        