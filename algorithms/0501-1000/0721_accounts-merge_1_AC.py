# https://leetcode.com/problems/accounts-merge/
# 1AC, search engine, index merging
# don't you think that's too much work for 10 minutes?
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        idf = {}
        a = accounts
        n = len(a)

        # inverte index
        for i, x in enumerate(a):
            nx = len(x)
            for j in range(1, nx):
                em = x[j]
                if not em in idf:
                    idf[em] = set()
                idf[em].add(i)

        ds = [i for i in range(n)]

        # disjoint set
        def findRoot(ds, x):
            r = x
            while r != ds[r]:
                r = ds[r]
            k = x
            while x != r:
                x = ds[x]
                ds[k] = r
                k = x
            return r

        for em in idf:
            ai = list(idf[em])
            ni = len(ai)
            r1 = findRoot(ds, ai[0])
            for i in range(1, ni):
                r2 = findRoot(ds, ai[i])
                ds[r2] = r1
        res ={}
        for i in range(n):
            ri = findRoot(ds, i)
            if not ri in res:
                res[ri] = (a[ri][0], set())
            ems = res[ri][1]
            ni = len(a[i])
            for j in range(1, ni):
                ems.add(a[i][j])
        return [[x[0]] + sorted(x[1]) for x in res.values()]
