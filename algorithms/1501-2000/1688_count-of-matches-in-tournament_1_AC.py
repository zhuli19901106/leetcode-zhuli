# easy
# https://leetcode.com/problems/count-of-matches-in-tournament/
# 1AC
class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n > 1:
            res += (n // 2)
            n = (n + 1) // 2
        return res
