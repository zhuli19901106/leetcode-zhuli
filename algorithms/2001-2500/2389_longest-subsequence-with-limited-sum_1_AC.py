# easy
# https://leetcode.com/problems/longest-subsequence-with-limited-sum/
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        a = sorted(nums)
        n = len(a)
        for i in range(n - 1):
            a[i + 1] += a[i]

        res = []
        for q in queries:
            if q >= a[-1]:
                res.append(n)
                continue
            if q < a[0]:
                res.append(0)
                continue
            ll, rr = 0, n - 1
            while rr - ll > 1:
                mm = ll + (rr - ll) // 2
                if q < a[mm]:
                    rr = mm
                else:
                    ll = mm
            res.append(rr)
        return res
