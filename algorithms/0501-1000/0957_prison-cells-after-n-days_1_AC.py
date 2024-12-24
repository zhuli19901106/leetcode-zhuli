# medium
# https://leetcode.com/problems/prison-cells-after-n-days/
# 1AC, cellular automata, find the cycle length
class Solution:
    M = 8

    def __init__(self):
        trans = [-1 for i in range(2 ** Solution.M)]
        n = len(trans)
        for i in range(n):
            i1 = 0
            for j in range(1, M - 1):
                if bool(i & (1 << j - 1)) == bool(i & (1 << j + 1)):
                    i1 |= (1 << j)
            trans[i] = i1
        self.trans = trans

    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        x = 0
        for b in cells:
            x = (x << 1) | b
        mm = {}
        arr = []
        i = 0
        cl = None
        while i <= N:
            if not x in mm:
                mm[x] = i
                arr.append(x)
                x = self.trans[x]
                i += 1
                continue
            if cl is None:
                cl = i - mm[x]
                N = mm[x] + (N - mm[x]) % cl
                break
        x = arr[N]
        res = []
        for _ in range(Solution.M):
            res.append(x & 1)
            x >>= 1
        res = res[::-1]
        return res
