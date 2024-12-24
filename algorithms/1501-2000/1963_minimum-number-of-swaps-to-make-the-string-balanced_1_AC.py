# medium
# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/
# more of a teaser than a test
class Solution:
    def minSwaps(self, s: str) -> int:
        cnt = 0
        min_val = 0
        for c in s:
            if c == '[':
                cnt += 1
            elif c == ']':
                cnt -= 1

            if cnt < min_val:
                min_val = cnt

        return (-min_val + 1) // 2
