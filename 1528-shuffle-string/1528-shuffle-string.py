class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        t = [0] * len(s)
        for string, index in zip(s,indices):
            t[index] = string
        return "".join(t)
        


        