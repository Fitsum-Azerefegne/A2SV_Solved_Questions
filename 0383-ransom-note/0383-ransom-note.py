class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter_rans = Counter(ransomNote)
        counter_mag = Counter(magazine)
        for letter in counter_rans:
            if counter_rans[letter] > counter_mag[letter]:
                return False
        return True        