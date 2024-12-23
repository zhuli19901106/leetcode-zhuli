# https://leetcode.com/problems/count-nodes-with-the-highest-score/
# a bit tiring, but not difficult
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        g = {}
        n = len(parents)
        for i, p in enumerate(parents):
            if not i in g:
                g[i] = set()
            if p == -1:
                continue

            if not p in g:
                g[p] = set()
            g[p].add(i)

        res = {}
        vst = set()
        self.traverse(0, g, n, vst, res)

        max_prod = max(res.values())
        return len([x for x, prod in res.items() if prod == max_prod])

    def traverse(self, x, g, n, vst, res):
        vst.add(x)
        if x not in g or len(g[x]) == 0:
            res[x] = n - 1
            return 1

        prod = 1
        cc = 1
        for y in g[x]:
            if y in vst:
                continue
            cc1 = self.traverse(y, g, n, vst, res)
            cc += cc1
            prod *= cc1

        # except the root
        if n - cc > 0:
            prod *= n - cc
        res[x] = prod

        return cc
