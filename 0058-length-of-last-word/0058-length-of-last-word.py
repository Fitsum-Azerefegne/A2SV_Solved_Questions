class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        if words:
            last_word = words[-1]
            return len(last_word) 
        return 0
    