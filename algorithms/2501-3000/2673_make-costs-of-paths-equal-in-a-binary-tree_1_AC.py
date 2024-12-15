# https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/
# somewhat tricky, but not too difficult
class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        path_cost = [0 for i in range(n)]
        self.calcPathCost(0, n, cost[0], cost, path_cost)

        res = [0 for i in range(n)]
        self.traverse(0, n, path_cost, res)
        return sum(res)

    def calcPathCost(self, x, n, cur_cost, cost, path_cost):
        xl, xr = x * 2 + 1, (x + 1) * 2
        if xl >= n and xr >= n:
            path_cost[x] = cur_cost

        if xl < n:
            self.calcPathCost(xl, n, cur_cost + cost[xl], cost, path_cost)
        if xr < n:
            self.calcPathCost(xr, n, cur_cost + cost[xr], cost, path_cost)

    def traverse(self, x, n, path_cost, res):
        xl, xr = x * 2 + 1, (x + 1) * 2
        if xl >= n and xr >= n:
            return path_cost[x]

        cl = self.traverse(xl, n, path_cost, res)
        cr = self.traverse(xr, n, path_cost, res)
        res[x] += max(cl, cr) - min(cl, cr)

        return max(cl, cr)
