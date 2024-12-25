# hard
# https://leetcode.com/problems/valid-arrangement-of-pairs/
# got a relatively simple recursive solution, but TLE
# it should be O(E) for graph traversing, but with the list += operations, it's no longer O(E)
# after checking this, I'm actually doing Hierholzter's algorithm without even learning it
# https://www.geeksforgeeks.org/hierholzers-algorithm-directed-graph/
# really hard
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        ind, outd = {}, {}
        g = {}
        for x, y in pairs:
            if not x in ind:
                ind[x] = outd[x] = 0
            if not y in ind:
                ind[y] = outd[y] = 0
            outd[x] += 1
            ind[y] += 1

            if not x in g:
                g[x] = []
            if not y in g:
                g[y] = []
            g[x].append(y)

        # pick a node that's guaranteed to traverse everything
        sx = -1
        for x in g:
            if sx == -1:
                sx = x
            if outd[x] - ind[x] == 1:
                sx = x
                break

        res = []
        self.traverse(sx, g, res)
        res = res[::-1]
        return res

    def traverse(self, x, g, res):
        while len(g[x]) > 0:
            y = g[x].pop()
            self.traverse(y, g, res)
            res.append([x, y])

'''
    def traverse(self, x, g):
        res = []
        while len(g[x]) == 1:
            y = g[x].pop()
            res.append([x, y])
            x = y

        # there can be many loops
        loops = []
        # there should be at most one chain
        chains = []
        while len(g[x]) > 0:
            y = g[x].pop()

            res1 = self.traverse(y, g)
            if len(res1) > 0 and res1[-1][1] == x:
                loops.append((y, res1))
            else:
                chains.append((y, res1))
        # this should be the slow part
        for y, loop in loops:
            res.append([x, y])
            res += loop

        for y, chain in chains:
            res.append([x, y])
            res += chain

        return res
'''
