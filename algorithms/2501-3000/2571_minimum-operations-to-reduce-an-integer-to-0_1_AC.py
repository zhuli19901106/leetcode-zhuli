# medium
# https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/
# edge cases
class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        carry = False
        while n != 0:
            if n & 1 == 0:
                n >>= 1
                continue

            c1 = 1 if carry else 0
            while n > 0 and n & 1 == 1:
                n >>= 1
                c1 += 1
            if c1 == 1:
                res += c1
                carry = False
                continue

            c0 = 0
            while n > 0 and n & 1 == 0:
                n >>= 1
                c0 += 1

            # one special case
            if c0 == 1:
                res += 1
                carry = True
            else:
                res += min(c1, 2)
                carry = False

        return res
