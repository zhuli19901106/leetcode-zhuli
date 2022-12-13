# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        p = prices
        n = len(p)
        res = 0
        i = 0
        while i < n:
            j = i + 1
            while j < n and p[j] == p[j - 1] - 1:
                j += 1
            res += (j - i) * (j - i + 1) // 2
            i = j

        return res
