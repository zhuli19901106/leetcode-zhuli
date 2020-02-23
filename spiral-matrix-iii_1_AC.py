# https://leetcode.com/problems/spiral-matrix-iii/
# pure simulation logic
class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        n, m = R, C
        offs = [(0, +1), (+1, 0), (0, -1), (-1, 0)]

        def inbound(x, y):
            return x >= 0 and x <= n - 1 and y >= 0 and y <= m - 1

        res = []
        direc = 0
        step = 1
        si = 0
        num_iter = 0
        x, y = r0, c0
        while len(res) < n * m:
            if inbound(x, y):
                res.append([x, y])
            elif (direc == 0 and y > m - 1) or (direc == 1 and x > n - 1) or\
                (direc == 2 and y < 0) or (direc == 3 and x < 0):
                x += (step - si) * offs[direc][0]
                y += (step - si) * offs[direc][1]
                si = step

            if si == step:
                direc = (direc + 1) % len(offs)
                si = 0
                num_iter += 1
                if num_iter == 2:
                    step += 1
                    num_iter = 0
            x += offs[direc][0]
            y += offs[direc][1]
            si += 1
        return res
