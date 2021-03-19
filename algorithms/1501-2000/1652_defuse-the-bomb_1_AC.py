# https://leetcode.com/problems/defuse-the-bomb/
# 1AC, a bit of wrap around to do
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0 for _ in range(n)]
        if k == 0:
            return res

        arr = code * 3
        ps_arr = [0]
        for i in range(len(arr)):
            ps_arr.append(ps_arr[-1] + arr[i])

        if k > 0:
            for i in range(n):
                res[i] = ps_arr[n + i + k + 1] - ps_arr[n + i + 1]
        else:
            for i in range(n):
                res[i] = ps_arr[n + i] - ps_arr[n + i + k]
        return res
