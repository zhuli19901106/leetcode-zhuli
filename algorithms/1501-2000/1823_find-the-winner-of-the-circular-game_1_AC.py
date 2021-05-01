# https://leetcode.com/problems/find-the-winner-of-the-circular-game/
# 1AC, Josephus circle, 1-indexed
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        res = 1
        for i in range(2, n + 1):
            res = (res + k - 1) % i + 1
        return res
