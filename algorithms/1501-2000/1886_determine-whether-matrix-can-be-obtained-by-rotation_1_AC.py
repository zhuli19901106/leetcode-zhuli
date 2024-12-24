# easy
# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/
# 1AC, brute-force

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        for _ in range(4):
            f = True
            i = 0
            while f and i < n:
                j = 0
                while f and j < n:
                    if mat[i][j] != target[i][j]:
                        f = False
                    j += 1
                i += 1
            if f:
                return True
            mat = self.rotate(mat)
        return False
    
    def rotate(self, m1):
        n = len(m1)
        m2 = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                m2[j][n - 1 - i] = m1[i][j]
        return m2
