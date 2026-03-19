class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        def pow(x, n):
            result = 1           
            while n > 0:        
                if n % 2 == 1:   
                    result = (result * x) % MOD  
                x = (x * x) % MOD 
                n //= 2          
            return result

        even = (n + 1) // 2  
        odd = n // 2 
        return (pow(5,even) * pow(4, odd)) % MOD