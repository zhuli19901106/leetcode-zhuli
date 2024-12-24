# easy
# https://leetcode.com/problems/special-positions-in-a-binary-matrix/
# 1AC
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        ar = [0 for _ in range(n)]
        ac = [0 for _ in range(m)]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    ar[i] += 1
                    ac[j] += 1
        res = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] != 1:
                    continue
                if ar[i] == 1 and ac[j] == 1:
                    res += 1
        return res
