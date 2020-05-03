# https://leetcode.com/problems/queries-on-a-permutation-with-key/
# https://leetcode.com/problems/queries-on-a-permutation-with-key/discuss/575208/Java-Binary-indexed-tree-solution
# 1AC, a clever solution using BIT
class BIT:
    def __init__(self, n):
        self.a = [0 for i in range(n + 1)]
        self.n = n

    def add(self, idx, val):
        a = self.a
        n = self.n
        if idx < 1 or idx > n:
            return
        i = idx
        while i <= n:
            a[i] += val
            i += (i & -i)

    def sum(self, idx):
        if idx < 1:
            return 0
        a = self.a
        n = self.n
        idx = min(idx, n)

        res = 0
        i = idx
        while i > 0:
            res += a[i]
            i -= (i & -i)
        return res

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        nq = len(queries)
        bit = BIT(nq + m)
        mm = {}
        for i in range(1, m + 1):
            bit.add(nq + i, 1)
            mm[i] = nq + i

        res = []
        j = nq
        for q in queries:
            i = mm[q]
            # number of elements before it
            res.append(bit.sum(i) - 1)
            bit.add(i, -1)

            # relocate it to the front
            mm[q] = j
            bit.add(j, 1)
            j -= 1
        return res
