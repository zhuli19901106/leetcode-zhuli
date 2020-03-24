# https://leetcode.com/problems/flip-string-to-monotone-increasing/
# 1AC, standard practice
class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        n = len(S)
        if n < 2:
            return 0

        a1 = [0 for i in range(n)]
        a2 = [0 for i in range(n)]

        sm = 0
        for i in range(n):
            a1[i] = sm
            sm += 1 if S[i] == '1' else 0
        sm = 0
        for i in range(n - 1, -1, -1):
            a2[i] = sm
            sm += 1 if S[i] == '0' else 0
        res = n
        for i in range(n):
            res = min(res, a1[i] + a2[i])
        return res
