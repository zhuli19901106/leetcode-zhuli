# medium
# https://leetcode.com/problems/smallest-common-region/
# LCA problem
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        mm = {}
        for ar in regions:
            n = len(ar)
            for i in range(1, n):
                mm[ar[i]] = ar[0]
        x = region1
        a1 = [x]
        while x in mm:
            x = mm[x]
            a1.append(x)
        x = region2
        a2 = [x]
        while x in mm:
            x = mm[x]
            a2.append(x)
        i1 = len(a1) - 1
        i2 = len(a2) - 1
        while i1 > 0 and i2 > 0 and a1[i1 - 1] == a2[i2 - 1]:
            i1 -= 1
            i2 -= 1
        return a1[i1]
