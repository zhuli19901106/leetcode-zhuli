# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        i = 0
        j = 0
        while j < n:
            if i >= n or arr[i] != arr[j]:
                if i - j > n // 4:
                    return arr[j]
                else:
                    j = i
            i += 1
        return None
