# easy
# https://leetcode.com/problems/number-of-equivalent-domino-pairs/
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        m = {}
        R = 10
        res = 0
        for x, y in dominoes:
            k1 = x * R + y
            if k1 in m:
                res += m[k1]
            k2 = y * R + x
            if k2 != k1 and k2 in m:
                res += m[k2]
            if k1 in m:
                m[k1] += 1
            else:
                m[k1] = 1
        return res
