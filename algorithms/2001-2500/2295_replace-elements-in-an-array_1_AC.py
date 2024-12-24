# medium
# https://leetcode.com/problems/replace-elements-in-an-array/
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        a = nums
        mm = {}
        for i, x in enumerate(a):
            mm[x] = i
        for x, y in operations:
            if not x in mm:
                continue
            i = mm[x]
            del mm[x]

            # NOTE: after each op the array is still distinct
            mm[y] = i
            a[i] = y

        return a
