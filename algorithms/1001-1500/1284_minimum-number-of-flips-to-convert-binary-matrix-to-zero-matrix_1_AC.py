# hard
# https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/
# extremely simple idea, but a bit dirty work to encode the matrices
from collections import deque

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        OFFS = [(-1, 0), (+1, 0), (0, 0), (0, -1), (0, +1)]
        FLIPS = []

        # create bit masks for flip operations
        a = mat
        n, m = len(a), len(a[0])
        for i in range(n):
            for j in range(m):
                mask = 0
                for off in OFFS:
                    i1, j1 = i + off[0], j + off[1]
                    if i1 < 0 or i1 > n - 1 or j1 < 0 or j1 > m - 1:
                        continue
                    mask |= (1 << (i1 * m + j1))
                FLIPS.append(mask)

        mask0 = 0
        for i in range(n):
            for j in range(m):
                if a[i][j] == 0:
                    continue
                mask0 |= (1 << (i * m + j))

        mm = {}
        q = deque()

        mm[mask0] = 0
        q.append(mask0)
        while len(q) > 0 and (not 0 in mm):
            mask = q.popleft()
            val = mm[mask]
            for flip in FLIPS:
                mask1 = mask ^ flip
                if mask1 in mm:
                    continue
                mm[mask1] = val + 1
                q.append(mask1)

        return mm[0] if 0 in mm else -1
