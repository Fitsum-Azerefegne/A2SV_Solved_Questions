class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        output = ""
        for char, freq in count.most_common():
            output += char * freq

        return output
         
        
        