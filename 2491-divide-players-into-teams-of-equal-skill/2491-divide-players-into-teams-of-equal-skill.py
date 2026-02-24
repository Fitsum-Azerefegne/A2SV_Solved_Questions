class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill =sorted(skill)
        left = 0
        right = len(skill) - 1
        chemistry = 0
        skills = skill[left] + skill[right]
        while left < right:
            if skills != skill[left] + skill[right]:
                return -1
            chemistry += (skill[left] * skill[right])
            left += 1
            right -= 1
        return chemistry

          