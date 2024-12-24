# medium
# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/
class Solution:
    def findScore(self, nums: List[int]) -> int:
        a = [(x, i) for i, x in enumerate(nums)]
        n = len(a)
        b = [False for i in range(n)]

        res = 0
        a.sort()
        for x, i in a:
            if b[i]:
                continue

            b[i] = True
            res += x
            if i > 0:
                b[i - 1] = True
            if i < n - 1:
                b[i + 1] = True
        return res
