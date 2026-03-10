class Solution:
    def isValid(self, s: str) -> bool:
        bracket_hash = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        stack = []
        for t in s:
            if t in bracket_hash :
                if not stack:
                    return False
                front = stack.pop()
                if bracket_hash[t] != front:
                    return False
            else:
                stack.append(t)
        if len(stack) != 0:
            return False
        return True




        