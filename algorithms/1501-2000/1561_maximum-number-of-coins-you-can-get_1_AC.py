# medium
# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
# 1AC, greedy
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        a = sorted(piles)
        n = len(a)
        return sum(a[n // 3: n: 2])
