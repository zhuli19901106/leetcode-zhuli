# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/
# 1AC, count it
from collections import defaultdict

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        mm = defaultdict(int)
        n, m = len(bank), len(bank[0])
        for i in range(n):
            cc = 0
            for j in range(m):
                if bank[i][j] == '1':
                    cc += 1
            if cc > 0:
                mm[i] = cc
        ac = []
        for i in sorted(mm.keys()):
            ac.append(mm[i])

        nc = len(ac)
        res = 0
        for i in range(nc - 1):
            res += ac[i] * ac[i + 1]
        return res
