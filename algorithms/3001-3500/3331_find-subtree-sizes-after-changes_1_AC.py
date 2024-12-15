# https://leetcode.com/problems/find-subtree-sizes-after-changes/
# sort of a hard medium, even harder due to very confusing description
# do a path compression like disjoint sets, then traverse to count nodes
# careful, simultaneously
# this is too much for a medium
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        tr = self.constructTree(parent)

        n = len(parent)
        next_par = [None for i in range(n)]

        self.changeTree(tr, 0, s, next_par)
        for i in range(n):
            if next_par[i] is None:
                next_par[i] = parent[i]
        next_tr = self.constructTree(next_par)

        res = [0 for i in range(n)]
        self.countTree(next_tr, 0, res)
        return res

    def constructTree(self, par):
        tr = {}
        for i, x in enumerate(par):
            if not i in tr:
                tr[i] = []
            if x != -1 and not x in tr:
                tr[x] = []

            if x != -1:
                tr[x].append(i)
        return tr

    def changeTree(self, tr, x, s, next_par):
        mx = {}
        cx = s[x]
        mx[cx] = []

        for y in tr[x]:
            my = self.changeTree(tr, y, s, next_par)
            for cy in my:
                if not cy in mx:
                    mx[cy] = []

                # different chars
                if cy != cx:
                    mx[cy] += my[cy]
                    continue
                
                # same char
                for y1 in my[cy]:
                    next_par[y1] = x

        mx[cx].append(x)
        return mx

    def countTree(self, tr, x, res):
        sm = 1
        for y in tr[x]:
            sm += self.countTree(tr, y, res)
        res[x] = sm
        return sm
