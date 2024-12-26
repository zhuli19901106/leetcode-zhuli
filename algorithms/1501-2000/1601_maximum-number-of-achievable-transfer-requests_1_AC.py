# hard
# https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/
# for these sizes of nv and ne, first thing come to mind was to BF
# seems it's acceptable, an easy hard
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        res = 0
        for bm in range(1 << len(requests)):
            cur = self.checkRequests(n, requests, bm)
            if cur == -1:
                continue
            res = max(res, cur)
        return res

    def checkRequests(self, n, rs, bm):
        cc = [0 for i in range(n)]
        for ri, r in enumerate(rs):
            if bm & (1 << ri) == 0:
                continue
            x, y = r
            cc[x] -= 1
            cc[y] += 1

        valid = True
        for i in range(n):
            if cc[i] != 0:
                valid = False
                break

        if not valid:
            return -1

        res = 0
        while bm != 0:
            bm &= bm - 1
            res += 1
        return res
