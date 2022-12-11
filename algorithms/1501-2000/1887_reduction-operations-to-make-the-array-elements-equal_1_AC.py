# https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        mm = {}
        for x in nums:
            if x in mm:
                mm[x] += 1
            else:
                mm[x] = 1
        a = list(mm.items())
        a.sort(reverse=True)

        res = 0
        n = len(a)
        for i in range(n - 1):
            res += (n - 1 - i) * a[i][1]

        return res
