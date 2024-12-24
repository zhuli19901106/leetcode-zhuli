# easy
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        cur_val = -1
        max_val = cur_val
        for i in range(n - 1, -1, -1):
            max_val = arr[i] if arr[i] > cur_val else cur_val
            arr[i] = cur_val
            cur_val = max_val
        return arr
