# medium
# https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        mm = {}
        for x in nums:
            if x in mm:
                mm[x] += 1
            else:
                mm[x] = 1
        res = []
        for x in mm:
            if mm[x] == 1 and not (x - 1 in mm or x + 1 in mm):
                res.append(x)

        return res
