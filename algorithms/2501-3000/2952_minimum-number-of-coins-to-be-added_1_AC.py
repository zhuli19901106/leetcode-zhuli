# https://leetcode.com/problems/minimum-number-of-coins-to-be-added/
# this is really tricky
# I take a look at my own code in Patching Array and say WTF
class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        n = len(coins)

        res = 0
        x = 0
        i = 0
        while i < n or x < target:
            if i < n and coins[i] <= x + 1:
                x += coins[i]
                i += 1
            else:
                x += x + 1
                res += 1

        return res
