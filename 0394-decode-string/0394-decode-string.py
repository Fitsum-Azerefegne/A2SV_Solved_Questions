class Solution:
    def decodeString(self, s: str) -> str:
        curr_string = ""
        stack = []
        repeat = 0
        for c in s:
            if c.isdigit():
                repeat = repeat * 10 + int(c)
            elif c == "[":
                
                stack.append((curr_string, repeat))
                repeat = 0
                curr_string = ""

            elif c == "]":
                front , count = stack.pop()
                curr_string = front + curr_string * count
            
            else:
                curr_string += c
        
        return curr_string
        