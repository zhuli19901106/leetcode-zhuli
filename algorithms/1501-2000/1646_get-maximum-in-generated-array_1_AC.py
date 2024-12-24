# easy
# https://leetcode.com/problems/get-maximum-in-generated-array/
# thy bidding
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        a = [0, 1]
        if n < 2:
            return n
        res = max(a)
        for i in range(2, n + 1):
            j = i // 2
            val = a[j] + a[j + 1] if i & 1 else a[j]
            res = max(res, val)
            a.append(val)
        return res
