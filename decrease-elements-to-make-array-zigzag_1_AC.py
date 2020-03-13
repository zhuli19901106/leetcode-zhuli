# https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/
# odd and even zigzags
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        a = nums
        n = len(a)

        res1 = 0
        for i in range(0, n, 2):
            val = 0
            if i > 0:
                val = max(val, a[i] - a[i - 1] + 1)
            if i < n - 1:
                val = max(val, a[i] - a[i + 1] + 1)
            res1 += val
        res2 = 0
        for i in range(1, n, 2):
            val = 0
            if i > 0:
                val = max(val, a[i] - a[i - 1] + 1)
            if i < n - 1:
                val = max(val, a[i] - a[i + 1] + 1)
            res2 += val
        return min(res1, res2)
