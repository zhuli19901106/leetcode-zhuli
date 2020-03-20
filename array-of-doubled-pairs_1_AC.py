# https://leetcode.com/problems/array-of-doubled-pairs/
# 1AC, sort by absolute value of keys
class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        mm = {}
        for x in A:
            if x in mm:
                mm[x] += 1
            else:
                mm[x] = 1

        ak = sorted(mm.keys(), key=lambda x: abs(x))
        for k in ak:
            v = mm[k]
            if v == 0:
                continue
            if 2 * k in mm and mm[2 * k] >= v:
                mm[k] -= v
                mm[2 * k] -= v
            else:
                return False
        return True
