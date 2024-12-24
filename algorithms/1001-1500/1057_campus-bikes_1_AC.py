# medium
# https://leetcode.com/problems/campus-bikes/
# 1AC, sort by edge length
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        ws = workers
        bs = bikes
        nw = len(ws)
        nb = len(bs)

        stw = set()
        stb = set()
        es = []
        for i in range(nw):
            for j in range(nb):
                es.append((abs(ws[i][0] - bs[j][0]) + abs(ws[i][1] - bs[j][1]), i, j))
        es.sort()
        res = [-1 for i in range(nw)]
        for d, i, j in es:
            if i in stw or j in stb:
                continue
            res[i] = j
            stw.add(i)
            stb.add(j)
        return res
