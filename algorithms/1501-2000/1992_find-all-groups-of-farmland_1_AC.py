# https://leetcode.com/problems/find-all-groups-of-farmland/
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        a = land
        n, m = len(a), len(a[0])
        res = []
        for i in range(n):
            for j in range(m):
                if a[i][j] == 0:
                    continue
                x = 1
                while i + x < n and a[i + x][j] == 1:
                    x += 1
                y = 1
                while j + y < m and a[i][j + y] == 1:
                    y += 1
                res.append([i, j, i + x - 1, j + y - 1])
                for ii in range(i, i + x):
                    for jj in range(j, j + y):
                        a[ii][jj] = 0

        return res
