# hard
# https://leetcode.com/problems/jump-game-v/
# after two failed attempts, I foumd this to be a graph problem
# build a graph and search for the longest path
# it worked, but need some memorization to speed up
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        g = {}
        for i in range(n):
            g[i] = set()

        for i in range(n):
            j = i - 1
            while i - j <= d and j >= 0 and arr[i] > arr[j]:
                g[i].add(j)
                j -= 1

            j = i + 1
            while j - i <= d and j <= n - 1 and arr[i] > arr[j]:
                g[i].add(j)
                j += 1

        res = {}
        a1 = [(x, i) for i, x in enumerate(arr)]
        # speed up here
        a1.sort()
        for x, i in a1:
            cur = self.findLongestPath(i, 1, g, res)
            res[i] = cur
        return max(res.values())

    def findLongestPath(self, x, cc, g, res):
        # speed up here
        if x in res:
            return res[x]

        cur = cc
        for y in g[x]:
            cc1 = self.findLongestPath(y, cc + 1, g, res)
            cur = max(cur, cc1 + 1)

        return cur
