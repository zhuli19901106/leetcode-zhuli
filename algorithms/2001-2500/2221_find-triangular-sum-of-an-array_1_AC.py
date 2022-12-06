# https://leetcode.com/problems/find-triangular-sum-of-an-array/
# calculating C(n, k) % 10 efficiently is a problem
# with 10 being composite, inverse doesn't always exist
# thus if O(n) complexity can't be achieved for all C(n, k)s, no point trying alternative thinking
# other than just a pure simulation
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            nums1 = []
            n = len(nums)
            for i in range(n - 1):
                nums1.append((nums[i] + nums[i + 1]) % 10)
            nums = nums1

        return nums[0]
