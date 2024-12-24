# medium
# https://leetcode.com/problems/maximum-rows-covered-by-columns/
# it's not greedy and I can't think of any smarter ways
# just BF, with some bit acceleration, of course
class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        g = matrix
        m, n = len(g), len(g[0])
        ar = [sum(r) for r in g]

        max_rc = 0
        for x in range(1 << n):
            if not self.countOnes(x) == numSelect:
                continue

            cc = [0 for i in range(m)]
            for j in range(n):
                d = x & 1
                x >>= 1
                if d == 0:
                    continue

                for i in range(m):
                    if g[i][j] == 1:
                        cc[i] += 1
            rc = len([i for i in range(m) if ar[i] == cc[i]])
            max_rc = max(max_rc, rc)

        return max_rc

    def countOnes(self, x):
        res = 0
        while x != 0:
            x &= x - 1
            res += 1
        return res
