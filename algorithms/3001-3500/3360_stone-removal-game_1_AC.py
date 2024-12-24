# easy
# https://leetcode.com/problems/stone-removal-game/
class Solution:
    def canAliceWin(self, n: int) -> bool:
        k = 10
        cc = 0
        while n >= k:
            n -= k
            k -= 1
            cc += 1
        return cc % 2 == 1
