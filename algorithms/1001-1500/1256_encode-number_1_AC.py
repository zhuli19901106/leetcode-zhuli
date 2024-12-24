# medium
# https://leetcode.com/problems/encode-number/
# 1AC, same idea, but three times the work with C++
class Solution:
    def encode(self, num: int) -> str:
        if num == 0:
            return ''
        n = num + 1
        bl = n.bit_length() - 1
        m = 1 << bl
        s = '{{:0{}b}}'.format(bl)
        s = s.format(n - m)
        return s
