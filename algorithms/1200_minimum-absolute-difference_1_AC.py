# https://leetcode.com/problems/minimum-absolute-difference/
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        a = sorted(arr)
        n = len(a)
        min_diff = a[1] - a[0]
        for i in range(n - 1):
            min_diff = min(min_diff, a[i + 1] - a[i])
        res = []
        for i in range(n - 1):
            if min_diff != a[i + 1] - a[i]:
                continue
            res.append([a[i], a[i + 1]])
        return res
