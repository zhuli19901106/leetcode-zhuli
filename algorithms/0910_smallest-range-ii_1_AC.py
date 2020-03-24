# https://leetcode.com/problems/smallest-range-ii/
# make it simple
class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        a = A
        k = K

        if k == 0:
            return max(a) - min(a)
        
        a.sort()
        n = len(a)
        res = a[n - 1] - a[0]
        for i in range(n - 1):
            a[i] += 2 * k
            cur_min = min(a[0], a[i + 1])
            cur_max = max(a[i], a[n - 1])
            res = min(res, cur_max - cur_min)
        return res
