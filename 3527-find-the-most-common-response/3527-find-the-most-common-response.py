class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:

        dd = defaultdict(int)
        responses = [list(set(response)) for response in responses]
        for response in responses:
            for i in range (len(response)):
                dd[response[i]] += 1
        max_value = max(dd.values())
        response_with_max = [response for response, freq in dd.items() if freq == max_value]
        response_with_max = sorted(response_with_max)  
        return(response_with_max[0])    