class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        last_value = 0
        roman_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
        for i in range(len(s) - 1, -1, -1):
            char = s[i]  
            value = roman_map[char] 
            if value < last_value:
                total -= value
            else:
                total += value
                
            last_value = value 

        return(total) 
        