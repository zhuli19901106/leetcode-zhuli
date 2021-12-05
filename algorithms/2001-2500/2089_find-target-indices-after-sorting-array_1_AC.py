# https://leetcode.com/problems/find-target-indices-after-sorting-array/
# 1AC

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        a = sorted(nums)
        res = []
        for i, x in enumerate(a):
            if x == target:
                res.append(i)
        return res
