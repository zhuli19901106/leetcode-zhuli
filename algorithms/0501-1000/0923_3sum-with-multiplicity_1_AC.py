# https://leetcode.com/problems/3sum-with-multiplicity/
# simple idea, intensive labor
class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        R = 3

        a = A
        a.sort()

        mm = {}
        for x in a:
            if x in mm:
                mm[x] += 1
            else:
                mm[x] = 1

        res = 0
        ak = list(mm.items())
        ak.sort()
        print(ak)
        
        def comb(n, k):
            res = 1
            for i in range(k):
                res *= n - i
                res //= i + 1
            return res

        def dfs(ak, i, path, sum_val, cnt):
            nonlocal res

            if cnt == R:
                if sum_val == target:
                    cur_res = 1
                    for vv, cc in path:
                        cur_res *= comb(mm[vv], cc)
                    res = (res + cur_res) % MOD
                return

            if i >= len(ak):
                return
            if sum_val + (R - cnt) * ak[i][0] > target:
                return

            for j in range(0, min(R - cnt, ak[i][1]) + 1):
                if j > 0:
                    path.append((ak[i][0], j))
                dfs(ak, i + 1, path, sum_val + ak[i][0] * j, cnt + j)
                if j > 0:
                    path.pop()

        dfs(ak, 0, [], 0, 0)
        return res
