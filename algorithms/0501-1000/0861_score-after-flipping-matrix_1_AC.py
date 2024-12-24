# medium
# https://leetcode.com/problems/score-after-flipping-matrix/
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        n = len(A)
        m = len(A[0])

        def flip(a, idx, rc):
            if rc == 0:
                for i in range(m):
                    a[idx][i] = 1 - a[idx][i]
            else:
                for i in range(n):
                    a[i][idx] = 1 - a[i][idx]

        for i in range(n):
            if A[i][0] == 0:
                flip(A, i, 0)
        for j in range(1, m):
            cnt = 0
            for i in range(n):
                if A[i][j] == 1:
                    cnt += 1
            if cnt < n - cnt:
                flip(A, j, 1)

        res = 0
        for i in range(n):
            val = 0
            for j in range(m):
                val = (val << 1) + A[i][j]
            res += val
        return res
