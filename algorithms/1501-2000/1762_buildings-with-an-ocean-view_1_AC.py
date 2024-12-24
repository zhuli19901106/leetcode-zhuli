# medium
# https://leetcode.com/problems/buildings-with-an-ocean-view/
# 1AC

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_val = 0
        n = len(heights)
        res = []
        for i in range(n - 1, -1, -1):
            if heights[i] > max_val:
                res.append(i)
            max_val = max(max_val, heights[i])
        return res[::-1]
