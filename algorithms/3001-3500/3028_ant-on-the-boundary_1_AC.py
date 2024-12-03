# https://leetcode.com/problems/ant-on-the-boundary/
# poor description
class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        pos = 0
        res = 0
        for x in nums:
            pos += x
            if pos == 0:
                res += 1
        return res
