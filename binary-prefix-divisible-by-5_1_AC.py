# https://leetcode.com/problems/binary-prefix-divisible-by-5/
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        val = 0
        for x in A:
            val = (val << 1) + x
            res.append(val % 5 == 0)
        return res
