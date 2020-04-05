# https://leetcode.com/problems/campus-bikes-ii/
# https://leetcode.com/problems/campus-bikes-ii/discuss/534671/Python-Self-illustrative-DFS-with-memorization
# got stuck on this for a long time, strange...
class Solution:
    INT_MAX = 2 ** 31 - 1

    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        aw = workers
        ab = bikes
        nw = len(aw)
        nb = len(ab)
        if nw == 0 or nw == 0:
            return 0
        ds = [[abs(aw[i][0] - ab[j][0]) + abs(aw[i][1] - ab[j][1])\
            for j in range(nb)] for i in range(nw)]
        dp = {}

        def dfs(wi, bk):
            nonlocal dp

            if wi == nw:
                return 0
            if (wi, bk) in dp:
                return dp[(wi, bk)]
            min_cur = Solution.INT_MAX
            for i in range(nb):
                if bk & (1 << i):
                    continue
                bk ^= (1 << i)
                cur = dfs(wi + 1, bk) + ds[wi][i]
                bk ^= (1 << i)
                min_cur = min(min_cur, cur)
            dp[(wi, bk)] = min_cur
            return min_cur

        return dfs(0, 0)
