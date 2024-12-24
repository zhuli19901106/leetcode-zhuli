# hard
# https://leetcode.com/problems/maximum-number-of-k-divisible-components/
# the point is, you should always split a subtree whenever it's k-divisible
# however you pick the root, doesn't matter
# greedy
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if sum(values) % k != 0:
            return -1

        g = {}
        for x, y in edges:
            if not x in g:
                g[x] = set()
            if not y in g:
                g[y] = set()
            g[x].add(y)
            g[y].add(x)

        res = [0]
        vst = set()
        # if it's a tree, it's supposed to be connected
        self.traverse(0, g, values, k, vst, res)
        return res[0]

    def traverse(self, x, g, values, k, vst, res):
        vst.add(x)
        smx = values[x]

        for y in g.get(x, set()):
            if y in vst:
                continue
            smy = self.traverse(y, g, values, k, vst, res)
            smx += smy

        if smx % k == 0:
            res[0] += 1
            return 0
        else:
            return smx
