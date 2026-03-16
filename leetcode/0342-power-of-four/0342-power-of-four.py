class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def function(n: int):
            if n == 4 or n == 1: 
                return 1
            if n <= 0 or n % 4 != 0:
                return None

            else:
                return function(n//4)
            
        val = function(n)
        return val == 1