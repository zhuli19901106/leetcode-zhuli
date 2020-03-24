# https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/
# Runtime: 20 ms, faster than 98.33% of Python3 online submissions for Minimum Swaps to Make Strings Equal.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Minimum Swaps to Make Strings Equal.
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        n = len(s1)
        nx = 0
        ny = 0
        for i in range(n):
            if s1[i] == s2[i]:
                continue
            if s1[i] == 'x':
                nx += 1
            elif s1[i] == 'y':
                ny += 1
        if (nx + ny) % 2 != 0:
            return -1
        res = nx // 2 + ny // 2
        if nx % 2 != 0 and ny % 2 != 0:
            res += 2
        return res
