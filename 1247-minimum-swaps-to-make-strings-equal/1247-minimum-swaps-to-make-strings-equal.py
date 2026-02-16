class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = yx = 0
        for a, b in zip(s1, s2):
            if a == 'x' and b == 'y':
                xy += 1
            elif a == 'y' and b == 'x':
                yx += 1

        if (xy + yx) % 2 != 0: # both added must be even or we get like situation ezample 3
            return -1  

        swaps = xy // 2 + yx // 2
        if xy % 2 == 1: # if xy is odd so is yx since we have checked on line 10
            swaps += 2

        return swaps
            