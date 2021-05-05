# https://leetcode.com/problems/count-submatrices-with-all-ones/
# 1AC, might feel a bit dizzy with indices
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        pre = [[0 for j in range(m)] for i in range(n + 1)]
        for i in range(n):
            for j in range(m):
                pre[i + 1][j] = pre[i][j] + mat[i][j]

        res = 0
        for i in range(n):
            for j in range(i, n):
                a = [pre[j + 1][k] - pre[i][k] for k in range(m)]
                k1 = 0
                t = j + 1 - i
                while k1 < m:
                    if a[k1] < t:
                        k1 += 1
                        continue
                    k2 = k1 + 1
                    while k2 < m and a[k2] == t:
                        k2 += 1
                    res += (k2 - k1) * (k2 - k1 + 1) // 2
                    k1 = k2
        return res
