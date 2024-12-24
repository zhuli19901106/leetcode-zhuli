# medium
# https://leetcode.com/problems/ugly-number-iii/
# 1AC, binary search, tricky though
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int: 
        def gcd(x, y):
            if x < y:
                return gcd(y, x)
            return x if y == 0 else gcd(y, x % y)

        def lcm(x, y):
            return x * y // gcd(x, y)

        def rank(x):
            return x // a + x // b + x // c - x // ab - x // bc - x // ca\
                + x // abc

        ab, bc, ca = lcm(a, b), lcm(b, c), lcm(c, a)
        abc = lcm(ab, c)

        low = 1
        high = 3 * 10 ** 9
        while low <= high:
            mid = low + (high - low) // 2
            r = rank(mid)
            if n < r:
                high = mid - 1
            elif n > r:
                low = mid + 1
            else:
                break
        x = mid
        x = max(x // a * a, x // b * b, x // c * c)
        return x
