# medium
# https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/
# 1AC, no trick, no trap
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        sum_add, max_shift = 0, 0
        for x in nums:
            add, shift = 0, 0
            while x != 0:
                if x & 1:
                    add += 1
                    x ^= 1
                else:
                    shift += 1
                    x >>= 1
            sum_add += add
            max_shift = max(max_shift, shift)
        return sum_add + max_shift
