# https://leetcode.com/problems/mirror-reflection/
# a bit hacky, needs some drawing and sketching
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        def gcd(x, y):
            if x == 0:
                return y
            if y == 0:
                return x
            return gcd(y % x, x)

        def lcm(x, y):
            return x * y  // gcd(x, y)

        if q == 0:
            return 0
        m = lcm(p, q)
        mp = m // p
        mq = m // q
        if mp % 2 == 0:
            return 0
        else:
            return 1 if mq % 2 == 1 else 2
