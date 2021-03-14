# https://leetcode.com/problems/decode-xored-array/
# 1AC
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        cur = first
        for x in encoded:
            cur ^= x
            res.append(cur)
        return res
