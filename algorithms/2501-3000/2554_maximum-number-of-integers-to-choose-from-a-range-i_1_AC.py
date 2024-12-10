# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/
# how is this "medium"?
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_st = set(banned)
        sm = 0
        res = 0
        for i in range(1, n + 1):
            if i in banned_st:
                continue
            if sm + i <= maxSum:
                sm += i
                res += 1
            else:
                break
        return res
