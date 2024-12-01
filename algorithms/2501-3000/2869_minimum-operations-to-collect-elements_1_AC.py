# https://leetcode.com/problems/minimum-operations-to-collect-elements/
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        st = set()
        res = 0
        for i in range(n - 1, -1, -1):
            x = nums[i]
            res += 1

            if x >= 1 and x <= k:
                st.add(x)
            if len(st) == k:
                break
        return res
