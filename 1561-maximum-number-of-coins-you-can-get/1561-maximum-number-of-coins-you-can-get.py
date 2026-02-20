class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)//3
        coins = 0
        division = 0
        for i in range(len(piles) - 2, -1, -2):
            coins += piles[i] 
            division += 1 
            if division == n:
                break
        return coins