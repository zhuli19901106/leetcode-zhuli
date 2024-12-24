# easy
# https://leetcode.com/problems/transpose-matrix/
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        n = len(A)
        m = len(A[0])
        B = [[0 for j in range(n)] for i in range(m)]
        for i in range(n):
            for j in range(m):
                B[j][i] = A[i][j]
        return B
