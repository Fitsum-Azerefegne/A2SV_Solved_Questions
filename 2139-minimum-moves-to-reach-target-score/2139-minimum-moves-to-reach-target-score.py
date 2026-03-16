class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        operation = 0
        while target > 1 :
            if maxDoubles == 0:
                return operation + target - 1
            if target % 2 == 0:
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1
            operation += 1
            
        return operation

        