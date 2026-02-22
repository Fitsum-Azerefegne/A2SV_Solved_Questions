class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block = False
        result = []
        buffer = ""

        for line in source:
            i = 0
            while i < len(line):
                if not in_block:
                    if line.startswith("//", i):
                        break
                    elif line.startswith("/*", i):
                        in_block = True
                        i += 2
                    else:
                        buffer += line[i]
                        i += 1

                else:
                    
                    if line.startswith("*/", i):
                        in_block = False
                        i += 2
                    else:
                        i += 1
            if not in_block and buffer:
                result.append(buffer)
                buffer = ""

        return result