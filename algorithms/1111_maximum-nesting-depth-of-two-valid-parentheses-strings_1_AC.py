# https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        max_cnt = 0
        cnt = 0
        for c in seq:
            if c == '(':
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            elif c == ')':
                cnt -= 1

        cnt = 0
        max_cnt //= 2
        res = []
        for c in seq:
            if c == '(':
                cnt += 1
                if cnt > max_cnt:
                    res.append(1)
                else:
                    res.append(0)
            elif c == ')':
                if cnt > max_cnt:
                    res.append(1)
                else:
                    res.append(0)
                cnt -= 1
        return res
