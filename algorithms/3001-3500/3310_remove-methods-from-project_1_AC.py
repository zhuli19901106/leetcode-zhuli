# https://leetcode.com/problems/remove-methods-from-project/
# simple graph search
# the example and description are really confusing, though
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = {}
        for x, y in invocations:
            if not x in g:
                g[x] = set()
            if not y in g:
                g[y] = set()
            g[x].add(y)

        bug = set()
        self.searchBug(k, g, bug)

        vst = set()
        isolate = True
        for x in range(n):
            if x in bug:
                continue
            ret = self.checkIsolation(x, g, bug, vst)
            if not ret:
                isolate = False
                break
        res = set(range(n))
        if isolate:
            res -= bug
        res = list(res)
        return res

    def searchBug(self, x, g, vst):
        vst.add(x)
        if not x in g:
            return

        for y in g[x]:
            if y in vst:
                continue
            self.searchBug(y, g, vst)

    def checkIsolation(self, x, g, bug, vst):
        vst.add(x)
        if x in bug:
            return False

        if not x in g:
            return True

        for y in g[x]:
            if y in vst:
                continue
            ret = self.checkIsolation(y, g, bug, vst)
            if not ret:
                return False
        return True
