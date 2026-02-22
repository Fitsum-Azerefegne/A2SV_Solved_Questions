class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        maximum = 0
        new_citation = []
        for h in citations:
            if h != 0 :
                new_citation.append(h)
        for i in range(len(new_citation)):
            research = 0   
            for j in range(len(new_citation)):
                if new_citation[j] >= new_citation[i]:
                    research += 1
            h = min(research, new_citation[i])
            maximum = max(maximum, h)  
        return maximum