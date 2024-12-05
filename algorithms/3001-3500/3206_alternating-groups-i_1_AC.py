# https://leetcode.com/problems/alternating-groups-i/
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        return len([i for i in range(n) if \
            colors[i] != colors[(i + n - 1) % n] and colors[i] != colors[(i + 1) % n]])
