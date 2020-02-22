# https://leetcode.com/problems/queens-that-can-attack-the-king/
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        N = 8

        def inbound(x, y):
            return x >= 0 and x <= N - 1 and y >= 0 and y <= N - 1

        offs = [(i // 3 - 1, i % 3 - 1) for i in range(9) if not i == 4]
        kx, ky = king

        qs = set()
        for qx, qy in queens:
            qs.add(qx * N + qy)

        res = []
        for off in offs:
            i = 1
            while True:
                x, y = kx + i * off[0], ky + i * off[1]
                if not inbound(x, y):
                    break
                if x * N + y in qs:
                    res.append([x, y])
                    break
                i += 1
        return res
