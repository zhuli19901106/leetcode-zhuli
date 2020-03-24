# https://leetcode.com/problems/rank-transform-of-an-array/
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_sorted = sorted(set(arr))
        m = dict([(x, i + 1) for i, x in enumerate(arr_sorted)])
        res = [m[x] for x in arr]
        return res
