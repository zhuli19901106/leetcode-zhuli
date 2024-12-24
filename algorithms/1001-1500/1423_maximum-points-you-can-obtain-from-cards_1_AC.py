# medium
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
# left x, right y, x + y = k, order doesn't matter
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        cs = cardPoints
        n = len(cs)
        suf = [0]
        for i in range(n - 1, n - k - 1, -1):
            suf.append(suf[-1] + cs[i])

        pref = 0
        res = suf[k]
        for i in range(k):
            pref += cs[i]
            res = max(res, pref + suf[k - i - 1])
        return res
