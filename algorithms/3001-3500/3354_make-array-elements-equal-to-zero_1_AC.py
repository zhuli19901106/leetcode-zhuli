# https://leetcode.com/problems/make-array-elements-equal-to-zero/
# not difficult, but tricky, multiple edge cases
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        sm = sum(nums)
        a = [(i, x) for i, x in enumerate(nums) if x != 0]
        if len(nums) > 0 and len(a) == 0:
            return 2 * len(nums)
        if len(nums) > 1 and len(a) == 1:
            return len(nums) - 1 if a[0][1] == 1 else 0

        res = 0
        m = len(a)
        sm1 = 0
        for j in range(m - 1):
            sm1 += a[j][1]
            if sm1 == sm - sm1 and a[j + 1][0] - a[j][0] > 1:
                res += 2 * (a[j + 1][0] - a[j][0] - 1)
            if abs(sm - 2 * sm1) == 1 and a[j + 1][0] - a[j][0] > 1:
                res += (a[j + 1][0] - a[j][0] - 1)
        return res
