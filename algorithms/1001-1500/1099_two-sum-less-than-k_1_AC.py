# https://leetcode.com/problems/two-sum-less-than-k/
# 1AC, sort and squeeze from both ends
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        a = A
        a.sort()
        n = len(a)
        i = 0
        j = n - 1
        res = -1
        for i in range(n):
            while j > i and a[i] + a[j] >= K:
                j -= 1
            if i >= j:
                break
            res = max(res, a[i] + a[j])
        return res
