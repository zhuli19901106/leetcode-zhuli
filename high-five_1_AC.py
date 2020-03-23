# https://leetcode.com/problems/high-five/
# 1AC
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        mm = {}
        for i, x in items:
            if not i in mm:
                mm[i] = []
            mm[i].append(x)
        res = []
        for i in sorted(mm.keys()):
            arr = sorted(mm[i], reverse=True)[:5]
            res.append([i, sum(arr) // len(arr)])
        return res
