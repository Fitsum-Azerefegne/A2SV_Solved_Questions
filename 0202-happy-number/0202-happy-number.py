class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  
        while n != 1 and n not in seen:
            seen.add(n)
            digits_int = [int(d) for d in str(n)]
            n = sum(num ** 2 for num in digits_int)  
        
        return n == 1
        