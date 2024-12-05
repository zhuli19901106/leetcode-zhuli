# https://leetcode.com/problems/maximum-height-of-a-triangle/
class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        return max(self.simulate([red, blue]), self.simulate([blue, red]))

    def simulate(self, a):
        f = 0
        n = 1
        while a[f] >= n:
            a[f] -= n
            f = 1 - f
            n += 1
        return n - 1
