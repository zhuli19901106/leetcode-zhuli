# easy
# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n, m = len(mat), len(mat[0])
        k %= m

        same = True
        for i in range(n):
            off = (m - k) % m if i % 2 == 0 else k
            for j in range(m):
                if mat[i][j] != mat[i][(j + off) % m]:
                    same = False
                    break
            if not same:
                break
        return same
