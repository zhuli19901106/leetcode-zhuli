# https://leetcode.com/problems/mean-of-array-after-removing-some-elements/
# 1AC
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        a = sorted(arr)
        n = len(a)
        nr = n // 20
        return sum(a[nr: -nr]) / (n - 2 * nr)
