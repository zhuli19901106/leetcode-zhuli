# https://leetcode.com/problems/maximum-score-after-splitting-a-string/
# 1AC
class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)

        c1 = [0 for i in range(n)]
        cc = 0
        for i in range(n):
            cc += 1 if s[i] == '0' else 0
            c1[i] = cc
        c2 = [0 for i in range(n)]
        cc = 0
        for i in range(n - 1, -1, -1):
            cc += 1 if s[i] == '1' else 0
            c2[i] = cc

        res = 0
        for i in range(n - 1):
            res = max(res, c1[i] + c2[i + 1])
        return res
