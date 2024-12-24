# medium
# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        mm = {}
        for x in nums:
            if not x in mm:
                mm[x] = 1
            else:
                mm[x] += 1

        a = []
        for x, cc in mm.items():
            a.append((cc, x))

        nr = max(mm.values())
        res = [[] for i in range(nr)]
        for cc, x in a:
            for i in range(cc):
                res[i].append(x)
        return res
