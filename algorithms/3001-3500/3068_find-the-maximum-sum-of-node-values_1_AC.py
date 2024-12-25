# hard
# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/
# think about it
# every time you pick a path u -> ... -> v to do XOR, only the values of u and v change
# the middles are left untouched
# thus, it should be simple
# it's a tree, you can go from any u to any v, see?
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        if n < 2:
            return sum(nums)

        st = []
        for i, x in enumerate(nums):
            if x < (x ^ k):
                st.append(i)

            if len(st) >= 2:
                i2 = st.pop()
                i1 = st.pop()
                nums[i1] ^= k
                nums[i2] ^= k

        if len(st) == 0:
            return sum(nums)

        i1 = st.pop()

        max_i, max_diff = -1, -int(1e9)
        for i, x in enumerate(nums):
            if i == i1:
                continue
            sm0 = nums[i1] + x
            # beware of precedence, damn
            sm1 = (nums[i1] ^ k) + (x ^ k)
            diff = sm1 - sm0
            if diff > max_diff:
                max_i, max_diff = i, diff
        if max_diff > 0:
            nums[i1] ^= k
            nums[max_i] ^= k

        return sum(nums)
