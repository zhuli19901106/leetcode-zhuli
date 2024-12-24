# medium
# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/
# sloppy
class Solution:
    def punishmentNumber(self, n: int) -> int:
        a = [i for i in range(1, n + 1) if self.isPunishment(i)]
        return sum([x * x for x in a])

    def isPunishment(self, x):
        return self.dfs(x * x, x)

    def dfs(self, x, t):
        if t == 0:
            return x == 0

        b10 = 1
        while b10 <= x:
            b10 *= 10
            x1, x2 = x // b10, x % b10
            if t < x2:
                break

            ret = self.dfs(x1, t - x2)
            if ret:
                return True
        return False
