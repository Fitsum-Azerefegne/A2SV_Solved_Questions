class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        output = ""
        dict_point = 0
        
        while dict_point < len(dictionary):
            s_pointer = 0          
            single_point = 0      
            while s_pointer < len(s) and single_point < len(dictionary[dict_point]):
                if s[s_pointer] == dictionary[dict_point][single_point]:
                    single_point += 1
                s_pointer += 1
            
            if single_point == len(dictionary[dict_point]):
                word = dictionary[dict_point]
                if len(word) > len(output) or ((len(word) == len(output) and word < output)):
                    output = word
            
            dict_point += 1   
        
        return output