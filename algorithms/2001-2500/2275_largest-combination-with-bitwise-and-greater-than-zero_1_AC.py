# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bits = 0
        for x in candidates:
            bits |= x

        res = 0
        while bits != 0:
            cur_bit = (bits & -bits)

            cnt = 0
            for x in candidates:
                if x & cur_bit != 0:
                    cnt += 1
            res = max(res, cnt)

            bits ^= cur_bit

        return res
