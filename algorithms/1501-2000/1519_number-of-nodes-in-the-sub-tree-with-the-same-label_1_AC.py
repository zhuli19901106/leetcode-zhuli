# medium
# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/
# just traverse and count
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        g = {}
        for x, y in edges:
            if not x in g:
                g[x] = set()
            if not y in g:
                g[y] = set()
            g[x].add(y)
            g[y].add(x)

        vst = set()
        res = [0 for i in range(n)]

        vst.add(0)
        self.traverse(0, g, labels, vst, res)

        return res

    def traverse(self, x, g, labels, vst, res):
        cx = labels[x]

        mx = {}
        mx[cx] = 1

        if not x in g:
            res[x] = 1
            return mx

        for y in g[x]:
            if y in vst:
                continue

            vst.add(y)
            my = self.traverse(y, g, labels, vst, res)

            for cy in my:
                if not cy in mx:
                    mx[cy] = 0
                mx[cy] += my[cy]
        res[x] = mx[cx]

        return mx
