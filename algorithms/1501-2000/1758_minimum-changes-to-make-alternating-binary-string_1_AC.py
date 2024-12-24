# easy
# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
# 1AC, simulation
class Solution:
    def minOperations(self, s: str) -> int:
        return min(self.check(s, 0), self.check(s, 1))

    def check(self, s, f):
        a = [int(c) for c in s]
        cc = 0
        for x in a:
            if x != f:
                cc += 1
            f = 1 - f
        return cc
