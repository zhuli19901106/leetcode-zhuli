# medium
# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/
# count max coverage times
# if you have to query and update at the same time, you'll need a BIT
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        max_val = max([y for x, y in intervals])
        cc = [0 for i in range(max_val + 1)]

        for x, y in intervals:
            cc[x - 1] -= 1
            cc[y] += 1

        res = 0
        sm = 0
        for i in range(max_val, -1, -1):
            sm += cc[i]
            cc[i] = sm
            res = max(res, sm)
        return res
