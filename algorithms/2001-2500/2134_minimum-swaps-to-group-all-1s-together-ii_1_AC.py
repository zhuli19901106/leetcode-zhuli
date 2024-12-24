# medium
# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/
# got stuck on this for over 30 minutes, found out that the swap doesn't have to be adjacent
# what a waste of time..
# actually quite easy
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        cc = nums.count(1)
        sm = sum(nums[: cc])
        res = cc - sm
        for i in range(cc, cc + n):
            sm += nums[i % n] - nums[i - cc]
            res = min(res, cc - sm)
        return res
