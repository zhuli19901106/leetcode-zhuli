# easy
# https://leetcode.com/problems/two-furthest-houses-with-different-colors/
# 1AC, brute-force

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        for k in range(n - 1, 0, -1):
            for i in range(n - k):
                if colors[i] != colors[i + k]:
                    return k
        return -1
