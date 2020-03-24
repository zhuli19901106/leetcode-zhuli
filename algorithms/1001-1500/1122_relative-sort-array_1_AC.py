# https://leetcode.com/problems/relative-sort-array/
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        m2 = dict((x, i) for i, x in enumerate(arr2))
        arr_idx1 = [m2[x] for x in arr1 if x in m2]
        head = [arr2[i] for i in sorted(arr_idx1)]
        tail = sorted([x for x in arr1 if not x in m2])
        return head + tail
