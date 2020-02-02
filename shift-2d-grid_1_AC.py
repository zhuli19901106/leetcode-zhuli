# https://leetcode.com/problems/shift-2d-grid/
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def shift(a, k):
            n = len(a)
            if n == 0 or k % n == 0:
                return a
            k %= n
            return a[k:] + a[:k]

        a = grid
        n = len(a)
        m = len(a[0])
        a1 = [a[i // m][i % m] for i in range(n * m)]
        a1 = shift(a1, n * m - k)
        res = [[a1[i * m + j] for j in range(m)] for i in range(n)]
        return res
