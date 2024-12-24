# medium
# https://leetcode.com/problems/candy-crush/
# 1AC, faithful simulation
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        b = board
        n = len(b)
        m = len(b[0])

        def eliminate():
            R = 3

            # eliminate row
            elim = set()
            for i in range(n):
                j = 0
                while j <= m - R:
                    if b[i][j] == 0:
                        j += 1
                        continue
                    k = j + 1
                    while k < m and b[i][j] == b[i][k]:
                        k += 1
                    if k - j >= 3:
                        for k1 in range(j, k):
                            elim.add((i, k1))
                    j = k

            # eliminate column
            for j in range(m):
                i = 0
                while i <= n - R:
                    if b[i][j] == 0:
                        i += 1
                        continue
                    k = i + 1
                    while k < n and b[i][j] == b[k][j]:
                        k += 1
                    if k - i >= 3:
                        for k1 in range(i, k):
                            elim.add((k1, j))
                    i = k

            ec = len(elim)
            if len(elim) == 0:
                return False
            for i, j in elim:
                b[i][j] = 0
            elim = set()

            # shift zeros upwards
            for j in range(m):
                k = n - 1
                for i in range(n - 1, -1, -1):
                    if b[i][j] == 0:
                        continue
                    b[k][j] = b[i][j]
                    k -= 1
                while k >= 0:
                    b[k][j] = 0
                    k -= 1

            return ec

        while eliminate() > 0:
            pass
        return b
