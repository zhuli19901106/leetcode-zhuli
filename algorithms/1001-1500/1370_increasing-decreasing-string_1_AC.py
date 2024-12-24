# easy
#https://leetcode.com/problems/increasing-decreasing-string/
class Solution:
    def sortString(self, s: str) -> str:
        ls = len(s)
        mm = {}
        for c in s:
            if c in mm:
                mm[c] += 1
            else:
                mm[c] = 1
        ks = sorted(mm.keys())
        nk = len(ks)
        res = []
        i1, i2 = 0, nk - 1
        while len(res) < ls:
            if i1 < i2:
                rg = range(i1, i2 + 1)
            else:
                rg = range(i1, i2 - 1, -1)
            for i in rg:
                if mm[ks[i]] == 0:
                    continue
                res.append(ks[i])
                mm[ks[i]] -= 1
            i1, i2 = i2, i1
        return ''.join(res)
