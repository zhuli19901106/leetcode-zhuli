# easy
# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/
# 1AC, sort and pick from largest
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        a = nums
        a.sort(reverse=True)
        s = sum(a)
        res = []
        cur = 0
        for x in a:
            cur += x
            res.append(x)
            if cur > s - cur:
                break
        return res
