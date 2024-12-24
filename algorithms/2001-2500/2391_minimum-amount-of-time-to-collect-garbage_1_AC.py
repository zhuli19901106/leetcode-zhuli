# medium
# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/
# stop the process as early as possible
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        R = 1 << 4
        MM_R = {'M': 8, 'P': 4, 'G': 0}

        def countGarbage(s):
            mm = {}
            for c in s:
                if c in mm:
                    mm[c] += 1
                else:
                    mm[c] = 1
            return (mm.get('M', 0) << 8) | (mm.get('P', 0) << 4) | (mm.get('G', 0))

        def getGarbage(x, c):
            return (R - 1) & (x >> MM_R[c])

        ag = [countGarbage(s) for s in garbage]
        res = 0
        n = len(ag)
        for c in 'MPG':
            remain = 0
            for x in ag:
                remain += getGarbage(x, c)
            for i, x in enumerate(ag):
                if remain == 0:
                    break

                cur = getGarbage(x, c)
                res += cur
                remain -= cur

                if remain == 0:
                    break

                if i < n - 1:
                    res += travel[i]

        return res

