# medium
# https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        res = []
        cur = 0
        mx = 0
        for x in nums:
            mx = max(mx, x)
            cur += x + mx
            res.append(cur)
        return res
