# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/
# topological sort
from collections import deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        g = {}
        ind = {}

        nr = len(recipes)
        for i in range(nr):
            r = recipes[i]
            if not r in g:
                g[r] = set()
                ind[r] = 0

            for ig in ingredients[i]:
                if not ig in g:
                    g[ig] = set()
                    ind[ig] = 0
                g[ig].add(r)
                ind[r] += 1

        for sp in supplies:
            if not sp in g:
                g[sp] = set()
                ind[sp] = 0

        q = deque()
        vst = set()
        for x in supplies:
            if ind[x] == 0:
                q.appendleft(x)

        while len(q) > 0:
            x = q.pop()
            vst.add(x)

            for y in g[x]:
                if y in vst:
                    continue

                ind[y] -= 1
                if ind[y] == 0:
                    q.appendleft(y)

        res = []
        for i in range(nr):
            full = True
            for ig in ingredients[i]:
                if not ig in vst:
                    full = False
                    break
            if full:
                res.append(recipes[i])
        return res
