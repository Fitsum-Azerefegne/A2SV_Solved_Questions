class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_sum = float('inf')
        res = []
        restaurant_hashmap = defaultdict(int)
        for i, n in enumerate(list1):
            restaurant_hashmap[n] = i
        for i, n in enumerate(list2):
            if n in restaurant_hashmap:
                curr_sum = restaurant_hashmap[n] + i
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    res = [n]
                elif curr_sum == min_sum:
                    res.append(n)
        return res 
