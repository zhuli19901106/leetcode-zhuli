# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
# 1AC
class Solution:
    def maxDepth(self, s: str) -> int:
        cnt, max_cnt = 0, 0
        for c in s:
            if c == '(':
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            elif c == ')':
                cnt -= 1
                if cnt < 0:
                    return -1
        return max_cnt
