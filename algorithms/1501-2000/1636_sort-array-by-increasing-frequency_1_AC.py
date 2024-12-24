# easy
# https://leetcode.com/problems/sort-array-by-increasing-frequency/
# 1AC
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mm = {}
        for x in nums:
            if x in mm:
                mm[x] += 1
            else:
                mm[x] = 1
        a = []
        for k, v in mm.items():
            a.append((k, v))
        a.sort(key=lambda x: (x[1], -x[0]))
        res = []
        for k, v in a:
            res += [k] * v
        return res
