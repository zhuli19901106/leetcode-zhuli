# https://leetcode.com/problems/min-max-game/
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        a = nums
        while len(a) > 1:
            n = len(a) // 2
            a1 = [0 for i in range(n)]
            for i in range(n):
                a1[i] = min(a[i << 1], a[(i << 1) + 1]) if i % 2 == 0 else max(a[i << 1], a[(i << 1) + 1])
            a = a1
        return a[0]
