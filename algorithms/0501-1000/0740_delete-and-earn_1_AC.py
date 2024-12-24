# medium
# https://leetcode.com/problems/delete-and-earn/
# 1AC, a good DP problem
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        mm = {}
        for x in nums:
            if x in mm:
                mm[x] += 1
            else:
                mm[x] = 1
        av = sorted(mm.keys())
        ac = [mm[x] for x in av]

        def dp(av, ac, i1, i2):
            loc1 = av[i1] * ac[i1]
            n = i2 - i1
            if n <= 1:
                return loc1
            loc2 = av[i1 + 1] * ac[i1 + 1]
            if n <= 2:
                return max(loc1, loc2)

            glob = loc1
            for i in range(2, n):
                tmp = loc2
                loc2 = glob + av[i1 + i] * ac[i1 + i]
                glob = max(loc1, tmp)
                loc1 = tmp
                res = max(loc2, glob)
            return res

        na = len(av)
        i = 0
        res = 0
        while i < na:
            j = i + 1
            while j < na and av[j] - av[j - 1] == 1:
                j += 1
            res += dp(av, ac, i, j)
            i = j
        return res
