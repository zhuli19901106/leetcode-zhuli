# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(x, y):
            while x != 0:
                x, y = y % x, x
            return y

        m = {}
        for x in deck:
            if x in m:
                m[x] += 1
            else:
                m[x] = 1
        d = None
        for x in m.values():
            if d is None:
                d = x
            else:
                d = gcd(d, x)
        return d != 1
