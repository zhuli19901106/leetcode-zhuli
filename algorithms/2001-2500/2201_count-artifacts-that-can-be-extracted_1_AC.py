# medium
# https://leetcode.com/problems/count-artifacts-that-can-be-extracted/
# count for total coverage and compare with the area of a rectangle
class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        g = [[0 for j in range(n)] for i in range(n)]
        for i, j in dig:
            g[i][j] = 1

        sm = [[0 for j in range(n + 1)] for i in range(n + 1)]
        for i in range(n):
            for j in range(n):
                sm[i + 1][j + 1] = sm[i + 1][j] + sm[i][j + 1] + g[i][j] - sm[i][j]

        res = 0
        for i1, j1, i2, j2 in artifacts:
            val = sm[i1][j1] + sm[i2 + 1][j2 + 1] - sm[i2 + 1][j1] - sm[i1][j2 + 1]
            if val == (i2 - i1 + 1) * (j2 - j1 + 1):
                res += 1
        return res
