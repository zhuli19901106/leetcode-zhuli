# easy
# https://leetcode.com/problems/three-consecutive-odds/
# 1AC
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        i = 0
        while i < n:
            j = i
            while j < n and arr[j] % 2 == 1:
                j += 1
            if j - i >= 3:
                return True
            i = j + 1
        return False
