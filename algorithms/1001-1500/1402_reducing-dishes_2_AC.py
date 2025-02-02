# hard
# https://leetcode.com/problems/reducing-dishes/
# this is greedy
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        a = satisfaction
        a.sort()

        res, cur, ps = 0, 0, 0
        n = len(a)
        for i in range(n - 1, -1, -1):
            ps += a[i]
            cur += ps
            res = max(res, cur)
        return res
