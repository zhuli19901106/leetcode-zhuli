# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
# 1AC
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        a = sorted(arr)
        dt = a[1] - a[0]
        for i in range(1, len(a) - 1):
            if a[i + 1] - a[i] != dt:
                return False
        return True
