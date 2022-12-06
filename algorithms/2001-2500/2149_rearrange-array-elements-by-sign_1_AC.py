# https://leetcode.com/problems/rearrange-array-elements-by-sign/
# don't wanna bother with O(1) space
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        t1 = []
        t2 = []
        for x in nums:
            if x > 0:
                t1.append(x)
            else:
                t2.append(x)

        n = len(nums) // 2
        j = 0
        for i in range(n):
            nums[j] = t1[i]
            j += 1
            nums[j] = t2[i]
            j += 1

        return nums
