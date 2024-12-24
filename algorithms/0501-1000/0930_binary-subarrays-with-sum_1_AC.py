# medium
# https://leetcode.com/problems/binary-subarrays-with-sum/
# 1AC, there's an exactly same problem before, right?
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        a = A
        n = len(a)
        mm = {0: 1}
        sum_val = 0
        res = 0
        for x in a:
            sum_val += x
            if sum_val - S in mm:
                res += mm[sum_val - S]
            if sum_val in mm:
                mm[sum_val] += 1
            else:
                mm[sum_val] = 1
        return res
