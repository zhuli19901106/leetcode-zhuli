# medium
# https://leetcode.com/problems/maximum-xor-for-each-query/
# 1AC, no trick
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        mask = (1 << maximumBit) - 1
        cur = 0
        ax = []
        for x in nums:
            cur ^= x
            ax.append(cur)

        res = []
        n = len(nums)
        for i in range(n):
            res.append(mask ^ ax[n - 1 - i])
        return res
