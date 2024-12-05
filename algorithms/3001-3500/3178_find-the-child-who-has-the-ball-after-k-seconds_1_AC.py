# https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/
class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        k %= 2 * (n - 1)
        if k <= n - 1:
            return k
        else:
            return 2 * (n - 1) - k
