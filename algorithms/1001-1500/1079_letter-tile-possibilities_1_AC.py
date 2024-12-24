# medium
# https://leetcode.com/problems/letter-tile-possibilities/
# Too much trouble.
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def fac(n):
            res = 1
            for i in range(1, n + 1):
                res *= i
            return res

        def combination(arr, cur_arr, cur_sum, target, res):
            if len(cur_arr) == len(arr):
                if cur_sum != target:
                    return
                res.append(cur_arr[:])
                return
            idx = len(cur_arr)
            if cur_sum > target:
                return
            idx = len(cur_arr)
            for i in range(arr[idx] + 1):
                if cur_sum + i > target:
                    break
                cur_arr.append(i)
                combination(arr, cur_arr, cur_sum + i, target, res)
                cur_arr.pop()

        def countPerm(arr):
            res = fac(sum(arr))
            for x in arr:
                if x != 0:
                    res //= fac(x)
            return res

        m = {}
        for c in tiles:
            if c in m:
                m[c] += 1
            else:
                m[c] = 1
        arr = list(m.values())
        res_comb = []
        for target in range(1, len(tiles) + 1):
            combination(arr, [], 0, target, res_comb)
        res = 0
        for comb in res_comb:
            res += countPerm(comb)
        return res
