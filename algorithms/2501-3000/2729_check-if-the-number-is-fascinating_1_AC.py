# https://leetcode.com/problems/check-if-the-number-is-fascinating/
class Solution:
    def isFascinating(self, n: int) -> bool:
        s = '{}{}{}'.format(n, 2 * n, 3 * n)
        st = set(s)
        return len(s) == 9 and len(st) == 9 and (not '0' in st)
