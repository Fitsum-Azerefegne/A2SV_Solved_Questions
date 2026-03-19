class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        x = 0
        added = 0
        i = 0
        while x < target:
            if i < len(coins) and coins[i] <= x + 1:
                x += coins[i]
                i += 1
            else:
                added += 1
                x += x + 1
        return added

        