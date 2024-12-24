# medium
# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        mg = {}
        res = []
        for i, sz in enumerate(groupSizes):
            if not sz in mg:
                mg[sz] = []
            mg[sz].append(i)
            if len(mg[sz]) == sz:
                res.append(mg[sz])
                mg[sz] = []
        return res
