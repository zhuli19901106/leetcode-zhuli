# medium
# https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/
# simple idea, like lexicographically sorted, but not exactly
class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        a = [(x, '{:b}'.format(x)) for x in nums]
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if a[i][1] + a[j][1] < a[j][1] + a[i][1]:
                    a[i], a[j] = a[j], a[i]

        res = int(''.join([tp[1] for tp in a]), 2)
        return res
