class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        total = 0
        for k, v in count.items():
            group = k + 1
            groups_needed = (v + group - 1) // group
            total += groups_needed * group       

        return total    