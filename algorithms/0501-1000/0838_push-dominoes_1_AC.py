# medium
# https://leetcode.com/problems/push-dominoes/
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        res = ['.' for i in range(n)]

        ds = []
        ds.append(('L', -1))
        for i, c in enumerate(dominoes):
            if c == '.':
                continue
            ds.append((c, i))
            res[i] = c
        ds.append(('R', n))
        m = len(ds)

        for i in range(m - 1):
            c1, c2 = ds[i][0], ds[i + 1][0]
            i1, i2 = ds[i][1], ds[i + 1][1]
            if c1 == c2:
                for j in range(i1 + 1, i2):
                    res[j] = c1
            elif c1 == 'R' and c2 == 'L':
                m1 = (i1 + i2 + 1) // 2
                m2 = (i1 + i2) // 2
                for j in range(i1 + 1, m1):
                    res[j] = c1
                for j in range(m2 + 1, i2):
                    res[j] = c2
        return ''.join(res)
