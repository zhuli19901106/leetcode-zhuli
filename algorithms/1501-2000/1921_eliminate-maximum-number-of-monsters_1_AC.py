# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/
# deal with the most urgent threat
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        a = [dist[i] / speed[i] for i in range(n)]
        a.sort()

        res = 0
        for i in range(n):
            # defeated
            if i >= a[i]:
                break
            else:
                res += 1
        return res
