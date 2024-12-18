# https://leetcode.com/problems/minimum-array-end/
# a "bit" tricky
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        cc = 0
        while (1 << cc) <= n:
            cc += 1

        ai = []
        i = 0
        while len(ai) < cc:
            if x & (1 << i) == 0:
                ai.append(i)
            i += 1

        n -= 1
        res = x
        for i in range(len(ai)):
            res |= ((n & 1) << ai[i])
            n >>= 1

        return res
