class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        for size in range(n, 1, -1):
            # Find the index of the largest num
            max_idx = arr.index(max(arr[:size]))
            
            if max_idx != size - 1:
                # Step1: Flip the largest num to the front
                if max_idx != 0:
                    arr[:max_idx+1] = arr[:max_idx+1][::-1]
                    res.append(max_idx + 1)  # record the flip
                
                # Step2: Flip it to correct position 
                arr[:size] = arr[:size][::-1]
                res.append(size)  # record the flip
        
        return res
        