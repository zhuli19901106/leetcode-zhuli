# medium
# https://leetcode.com/problems/find-champion-ii/
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        ind = {}
        for y in range(n):
            ind[y] = 0
        for x, y in edges:
            ind[y] += 1

        res = []
        for y, cc in ind.items():
            if cc == 0:
                res.append(y)
        return res[0] if len(res) == 1 else -1
