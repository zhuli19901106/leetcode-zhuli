# https://leetcode.com/problems/frog-jump-ii/
# this is really just mind trick

class Solution:
    def maxJump(self, stones: List[int]) -> int:
        a = stones
        n = len(a)
        res = 0

        if n >= 2:
            res = max(res, a[1] - a[0])
            for i in range(1, n - 2, 2):
                res = max(res, a[i + 2] - a[i])

        if n > 2:
            res = max(res,  a[2] - a[0])
            for i in range(2, n - 2, 2):
                res = max(res, a[i + 2] - a[i])

        return res
