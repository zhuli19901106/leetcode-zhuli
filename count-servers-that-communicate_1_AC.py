# https://leetcode.com/problems/count-servers-that-communicate/
# straightforward, but very clunky
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        def findRoot(m, x):
            if not x in m:
                m[x] = x
            r = x
            while r != m[r]:
                r = m[r]
            k = x
            while k != r:
                x = m[k]
                m[k] = r
                k = x
            return r

        a = grid
        n = len(a)
        m = len(a[0])
        ar = [[] for i in range(n)]
        ac = [[] for i in range(m)]
        ds = {}
        for i in range(n):
            for j in range(m):
                if a[i][j] == 1:
                    ar[i].append(j)
                    ac[j].append(i)
                    ds[i * m + j] = i * m + j
        for i in range(n):
            cnt = len(ar[i])
            if cnt < 2:
                continue
            for j in range(1, cnt):
                x1 = i * m + ar[i][0]
                x2 = i * m + ar[i][j]
                r1 = findRoot(ds, x1)
                r2 = findRoot(ds, x2)
                if r1 != r2:
                    ds[r1] = r2
        for i in range(m):
            cnt = len(ac[i])
            if cnt < 2:
                continue
            for j in range(1, cnt):
                x1 = ac[i][0] * m + i
                x2 = ac[i][j] * m + i
                r1 = findRoot(ds, x1)
                r2 = findRoot(ds, x2)
                if r1 != r2:
                    ds[r1] = r2
        for x in ds:
            findRoot(ds, x)

        rc = {}
        res = 0
        for _, v in ds.items():
            if v in rc:
                rc[v] += 1
            else:
                rc[v] = 1
        for _, v in rc.items():
            if v > 1:
                res += v
        return res
