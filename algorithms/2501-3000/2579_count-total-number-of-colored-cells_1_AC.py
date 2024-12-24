# medium
# https://leetcode.com/problems/count-total-number-of-colored-cells/
# isn't this pure math?
# (1, 1), (2, 5), (3, 13), (4, 25), ...
class Solution:
    def coloredCells(self, n: int) -> int:
        return 2 * n * n - 2 * n + 1
