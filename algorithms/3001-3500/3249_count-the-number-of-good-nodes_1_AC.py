# https://leetcode.com/problems/count-the-number-of-good-nodes/
class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = 0
        g = {}
        for x, y in edges:
            if not x in g:
                g[x] = set()
            if not y in g:
                g[y] = set()
            g[x].add(y)
            g[y].add(x)

            n = max(n, x + 1)
            n = max(n, y + 1)

        vst = set()
        res = set()
        self.traverse(0, g, vst, res)
        return len(res)

    def traverse(self, x, g, vst, res):
        if not x in g:
            res.add(x)
            return 1

        vst.add(x)

        cx = 1
        st = set()
        for y in g[x]:
            if y in vst:
                continue

            cy = self.traverse(y, g, vst, res)
            cx += cy
            st.add(cy)

        if len(st) <= 1:
            res.add(x)
        return cx
